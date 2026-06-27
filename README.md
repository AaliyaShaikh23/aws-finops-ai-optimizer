🚀 AI-Powered AWS FinOps Cost Optimization System
📌 Overview
This project is a serverless AI-powered FinOps system built using AWS services and Groq LLM.
It automatically monitors AWS infrastructure, analyzes cost usage, and generates intelligent optimization recommendations.
It helps identify:
Idle EC2 instances
Cost optimization opportunities
Estimated savings
Automated cloud usage reports

🏗️ Architecture
EventBridge (Scheduler)
        ↓
AWS Lambda
        ↓
EC2 + AWS Cost Explorer
        ↓
Groq AI (LLM Analysis)
        ↓
S3 (Store Report)
        ↓
SNS (Email Notification)

⚙️ Tech Stack
AWS Lambda (Serverless compute)
Amazon EC2 (Resource monitoring)
AWS Cost Explorer API (Billing analysis)
Amazon S3 (Report storage)
Amazon SNS (Email notifications)
Amazon EventBridge (Automation scheduler)
Python (Boto3)
Groq LLM API (AI cost analysis)

📌 Features
✔ Automated AWS cost monitoring
✔ EC2 instance analysis
✔ AI-powered optimization suggestions
✔ Cost saving estimation
✔ JSON report generation
✔ S3 report storage
✔ Email alerts via SNS
✔ Fully serverless architecture
✔ Scheduled execution using EventBridge

📂 Project Workflow
Lambda fetches EC2 instance details
Retrieves AWS cost data using Cost Explorer
Sends data to Groq AI for analysis
AI generates optimization suggestions
Report is saved in S3 bucket
SNS sends email notification with report
EventBridge runs this automatically daily

🧠 AI Capabilities
The system uses Groq LLM to:
Detect idle resources
Suggest cost optimization strategies
Estimate monthly savings
Provide FinOps recommendations

📦 AWS Permissions Required
Lambda execution role must include:
AmazonEC2ReadOnlyAccess
AWSCostExplorerReadOnlyAccess
AmazonS3FullAccess
AmazonSNSFullAccess
CloudWatchLogs permissions
🧪 Example Output
📊 AWS Data
{
  "ec2": [
    {
      "InstanceId": "i-xxxxxxxx",
      "State": "running",
      "Type": "t3.micro"
    }
  ],
  "cost": {
    "Amount": "12.34",
    "Unit": "USD"
  }
}

🤖 AI Response Sample
Identify idle EC2 instances
Recommend rightsizing
Suggest reserved instances
Estimated savings: ₹500–₹2000/month
📧 Output Delivery
📦 S3 Bucket → Stores full JSON report
📩 SNS → Sends email notification
📊 CloudWatch → Logs execution
🔐 Environment Variables

Set in Lambda:
GROQ_API_KEY = gsk_xxxxxxxxx
S3_BUCKET = aws-finops-report
SNS_TOPIC_ARN = arn:aws:sns:region:account-id:topic-name

🚀 How to Run
Deploy AWS Lambda function
Configure IAM permissions
Add Groq API key
Create S3 bucket
Create SNS topic & subscribe email
Set EventBridge schedule
Run Lambda test or wait for automation

📈 Real-World Use Case
This project simulates a FinOps automation system used in cloud engineering teams to:
Reduce AWS costs
Optimize unused resources
Automate cloud governance
Provide AI-driven insights

🏆 Key Learning Outcomes
Serverless architecture design
AWS service integration
IAM role configuration
Cloud cost optimization (FinOps)
AI integration in cloud systems
Event-driven automation

⭐ Future Improvements
Slack/Teams integration
Dashboard using Grafana
Multi-account AWS support
Real-time streaming alerts
Advanced AI cost forecasting

Author
Aaliya Shaikh
