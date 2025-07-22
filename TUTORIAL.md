URL Shortener App – Step-by-Step Tutorial

Table of Contents

Project Overview
Architecture Diagram
AWS Resources Needed
DynamoDB Table Setup
Lambda Function Setup
Create Lambda Function URL
Frontend Setup (S3 Static Site)
Connect Frontend & Test
Troubleshooting & Tips
Screenshots Checklist
1. Project Overview

This project is a minimal serverless URL shortener built with:

AWS Lambda (Python, logic and API)
DynamoDB (stores short URL mappings)
S3 (hosts the static frontend)
Users submit a long URL, receive a short URL, and when they visit the short URL, are redirected to the original site.

2. Architecture Diagram

User (Browser)
   ↓        ↑
 [Frontend (S3 Static Website)]
   ↓        ↑
 [AWS Lambda Function (Python)]
   ↓        ↑
 [DynamoDB Table (ShortUrls)]
3. AWS Resources Needed

DynamoDB table: ShortUrls
Lambda function: urlShortenerHandler (or similar)
Lambda Function URL (public endpoint)
S3 bucket (with static website hosting)
4. DynamoDB Table Setup

Go to AWS Console > DynamoDB > Create table.
Table name: ShortUrls
Partition key: id (String)
Capacity mode: On-demand
(Optional but best practice) Enable Point-in-time recovery
Create table
Screenshot: Table overview and settings.
5. Lambda Function Setup

Go to AWS Console > Lambda > Create function.
Name: urlShortenerHandler
Runtime: Python 3.11 or 3.12
Permissions: Use existing role (e.g., labrole)
Create the function.
Replace the default code with your lambda_function.py (with CORS support).
Set Environment Variables:
DDB_TABLE_NAME = ShortUrls
BASE_URL = (your Lambda Function URL, after creation)
Deploy/Save the function.
Screenshot: Lambda code, env variables, role settings.
6. Create Lambda Function URL

In Lambda function page, click “Function URL” tab (or button).
Click “Create function URL”.
Auth type: None (for lab/testing)
Copy the URL (e.g., https://xxxx.lambda-url.us-west-2.on.aws/)
Add this to your Lambda environment variable as BASE_URL.
Screenshot: Function URL.
7. Frontend Setup (S3 Static Site)

Go to AWS Console > S3 > Create bucket.
Bucket name: unique (e.g., nadia-url-shortener-2025)
Uncheck "Block all public access" (for lab only)
Create bucket.
Upload index.html and script.js from frontend/.
Go to Properties > Static website hosting
Enable
Index document: index.html
Go to Permissions > Bucket Policy
Add:
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME/*"
    }
  ]
}
Copy the website endpoint URL.
Screenshot: Bucket policy, static site settings, site in browser.
8. Connect Frontend & Test

In script.js, set:
const lambdaUrl = 'https://...lambda-url.../shorten';
Open S3 website endpoint in browser.
Submit a long URL, see short URL appear.
Click the short URL, confirm redirect.
Go to DynamoDB > Explore items, confirm mapping is saved.
Screenshot: Successful shorten, redirect, DynamoDB entry.
9. Troubleshooting & Tips

CORS Error?
Ensure Lambda responds with CORS headers (Access-Control-Allow-Origin: *).
See Lambda sample code for details.
403/Access Denied?
Make sure S3 bucket policy allows s3:GetObject.
Short URL doesn’t redirect?
Check Lambda GET logic.
Check mapping exists in DynamoDB.
No items in DynamoDB?
Check Lambda environment variable DDB_TABLE_NAME.
Check Lambda role permissions.
10. Screenshots Checklist

DynamoDB table created
Lambda code and environment variables
Lambda Function URL
S3 static website properties and policy
Frontend working (submit, get short URL, redirect)
DynamoDB with saved items

Good Lack !