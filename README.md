# CodeAlfa_data-Redundancy-Removal-System


## 1. Project Overview

This project prevents duplicate records from being
stored in a cloud database.

The application validates incoming records, normalizes
email addresses, and uses conditional database writes
to prevent duplicate insertions.

## 2. Objectives

- Identify duplicate records.
- Validate incoming data.
- Prevent duplicate database entries.
- Store unique records in the cloud.
- Improve database consistency.
- Monitor application activity.

## 3. Technologies Used

- Amazon EC2
- Amazon DynamoDB
- AWS IAM
- Amazon VPC
- Amazon CloudWatch
- AWS CloudTrail
- Python
- Boto3
- Git and GitHub

## 4. Architecture

Python application running on EC2
        |
        v
Input validation
        |
        v
Email normalization
        |
        v
DynamoDB conditional write
        |
        +---- New record: Insert
        |
        +---- Existing record: Reject

## 5. How It Works

1. Receive a record.
2. Validate the required fields.
3. Normalize the email address.
4. Attempt a conditional database write.
5. Insert unique records.
6. Reject duplicate records.
7. Monitor application activity.

## 6. Prerequisites

- An AWS account.
- An EC2 instance.
- An Amazon DynamoDB table.
- An IAM role with appropriate permissions.
- Python 3.
- Boto3.

## 7. Installation

Install the dependencies:

    python -m pip install -r requirements.txt

## 8. Configuration

The application expects a DynamoDB table named
UniqueRecords in the ap-south-1 region.

Configure AWS access through an appropriate IAM role
when running on EC2.

## 9. Run the Application

    python app.py

## 10. Testing

Submit both unique and duplicate records.

Verify that unique records are inserted and repeated
email addresses are rejected.

## 11. Expected Outcome

The system prevents duplicate insertions for the
configured unique identifier.

## 12. Author

Mohd Maaz
