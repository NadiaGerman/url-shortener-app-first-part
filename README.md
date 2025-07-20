# URL Shortener App

A minimal, serverless URL shortener app built with AWS Lambda, DynamoDB, and S3.  
Allows users to submit long URLs and receive a shareable short link.

---

## Features

- Shorten long URLs and share short links
- Redirection via Lambda
- Fully serverless: Lambda + DynamoDB + S3
- Ready for automation (Terraform, Jenkins)

---

## Project Structure

backend/ # Lambda function code (Python)
frontend/ # Static website (HTML + JS)
infra/ # Infrastructure-as-Code (Terraform, future)
screenshots/ # AWS setup screenshots for documentation


---

## Getting Started

See [PROJECT_PLAN.md](./PROJECT_PLAN.md) and [PRD.md](./PRD.md) for milestones and requirements.

---

## Lab/Manual Steps

Step-by-step setup and screenshots: see the tutorial section in this README (to be completed as you work).

---

## Automation

(Terraform and Jenkins integration planned; see `infra/` and `Jenkinsfile`)