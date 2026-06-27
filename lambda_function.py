import boto3
import json
import urllib3

ec2 = boto3.client('ec2')
ce = boto3.client('ce')
s3 = boto3.client('s3')
sns = boto3.client('sns')

http = urllib3.PoolManager()


# ---------------- EC2 ----------------
def get_ec2_instances():
    response = ec2.describe_instances()

    instances = []

    for r in response['Reservations']:
        for i in r['Instances']:
            instances.append({
                "InstanceId": i['InstanceId'],
                "State": i['State']['Name'],
                "Type": i['InstanceType']
            })

    return instances


# ---------------- COST ----------------
def get_cost():
    response = ce.get_cost_and_usage(
        TimePeriod={
            'Start': '2026-06-01',
            'End': '2026-06-27'
        },
        Granularity='MONTHLY',
        Metrics=['UnblendedCost']
    )

    return response['ResultsByTime']


# ---------------- AI ----------------
def analyze_with_ai(data):

    prompt = f"""
    You are an AWS FinOps expert.

    Analyze this AWS data:

    {json.dumps(data, indent=2)}

    Provide:
    - Idle resources
    - Cost saving suggestions
    - Estimated savings in INR
    """

    response = http.request(
        "POST",
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": "Bearer ",
            "Content-Type": "application/json"
        },
        body=json.dumps({
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        })
    )

    return json.loads(response.data.decode("utf-8"))


# ---------------- S3 ----------------
def upload_to_s3(report):

    s3.put_object(
        Bucket="aws-finops-report",
        Key="cost-report.json",
        Body=json.dumps(report),
        ContentType="application/json"
    )


# ---------------- SNS ----------------
def send_email(report):

    sns.publish(
        TopicArn="arn:aws:sns:ap-south-1:026898548339:CostOptimizationAlerts",
        Message=json.dumps(report, indent=2),
        Subject="AWS Cost Optimization Report"
    )


# ---------------- MAIN ----------------
def lambda_handler(event, context):

    print("FinOps Automation Started")

    ec2_data = get_ec2_instances()
    cost_data = get_cost()

    summary = {
        "ec2": ec2_data,
        "cost": cost_data
    }

    ai_response = analyze_with_ai(summary)

    report = {
        "summary": summary,
        "ai_analysis": ai_response
    }

    upload_to_s3(report)
    send_email(report)

    return {
        "statusCode": 200,
        "body": json.dumps("Report generated successfully")
    }