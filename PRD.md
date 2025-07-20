# Product Requirements Document – URL Shortener App

## Overview

A serverless app that allows users to shorten long URLs, share the short link, and redirect visitors to the original URL.

---

## Functional Requirements

- User can input a long URL and receive a short link.
- Visiting the short link redirects to the original URL.
- Links are stored and resolved via AWS DynamoDB.
- Lambda function provides both shortening and redirection endpoints.

---

## Non-Functional Requirements

- Secure input validation (prevent malicious URLs).
- Fast and highly available (serverless).
- All resources are created in AWS (lab environment).
- Frontend must be static, hosted on S3.

---

## Stretch Goals / Future Enhancements

- Custom aliases for short URLs.
- Analytics on clicks.
- Rate limiting and abuse prevention.
- Full automation with Terraform and CI/CD.

---

## Tech Stack

- AWS DynamoDB
- AWS Lambda (Python)
- AWS S3 (static site)
- GitHub (code repo)
- (Future) Terraform, Jenkins

---

## Success Criteria

- All core flows work as intended.
- App can be deployed and redeployed quickly in lab resets.
- Well-documented with screenshots and README.
