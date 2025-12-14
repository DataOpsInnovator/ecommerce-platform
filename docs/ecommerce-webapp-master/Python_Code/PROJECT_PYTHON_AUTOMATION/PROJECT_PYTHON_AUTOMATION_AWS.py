# Objective
# Enhance the AWS Lambda function to automate tasks involving S3, DynamoDB, SNS, SES, and CloudWatch. The function will:

# Trigger on S3 file uploads.
# Process file metadata and store it in DynamoDB.
# Notify via SNS about new file uploads.
# Send an email report using SES.
# Log events in CloudWatch for monitoring.


# AWS Services Overview
# S3: Source of event triggers.
# DynamoDB: Store processed file metadata.
# SNS (Simple Notification Service): Send notifications to subscribers (e.g., email, SMS).
# SES (Simple Email Service): Send detailed email reports.
# CloudWatch: Monitor and log function execution.
  
# Steps to Code:

# 1.S3 Integration
# Trigger Lambda when a file is uploaded.
# Parse the event payload to get bucket name and file details.
# Retrieve additional file metadata using the S3 head_object API.
  
# 2. DynamoDB Integration
# Create a table (e.g., FileMetadataTable) with attributes like FileName, BucketName, and ContentType.
# Use the DynamoDB client to insert metadata about the uploaded file.
  
# 3. SNS Integration
# Create an SNS topic (e.g., FileUploadNotifications).
# Add subscribers to the topic (e.g., email or SMS).
# In the Lambda function, publish a message to the SNS topic about the uploaded file.

# Comments for Code:
# # Use boto3.client('sns') to publish a message to the SNS topic
# # Include details like file name and bucket name in the message
# # Make sure the Lambda role has 'sns:Publish' permissions

# 4. SES Integration
# Configure SES to send emails (ensure the email address is verified in SES for sandbox environments).
# Compose an email report containing file details and metadata.
# Use SES to send the email to stakeholders.

# Comments for Code:
# # Use boto3.client('ses') to send an email
# # Specify sender and recipient email addresses
# # Include file metadata in the email body
# # Ensure the Lambda role has 'ses:SendEmail' permissions

# 5. CloudWatch Integration
# Add logging statements for each key step (e.g., S3 event received, DynamoDB insertion, SNS message sent).
# Use print() or logging for monitoring.
# Monitor the Lambda function’s execution logs in CloudWatch.
                      
# Comments for Code:
# # Use the logging module to log events at each step
# # Example: logging.info("Successfully processed file: %s", file_name)
# # View logs in the CloudWatch console for debugging and monitoring


# Part 2: Query Data with Athena:

# Create an S3 Data Catalog:
# Use Athena to point to the S3 bucket where the CSV or split files are stored.
# Define the schema for querying the data.
# Perform SQL queries on the data:

# Hints:
# Use the Athena console or boto3.client('athena') to execute SQL queries
# Set up an S3 bucket for Athena query results
# Example query: SELECT Category, SUM(Total) AS TotalSales FROM "sales_data_table" GROUP BY Category;


# Step 6: Visualize Data in QuickSight

# Connect QuickSight to Athena:
# Create a new data source pointing to the Athena table.
# Build dashboards:
# Visualize total sales by category, trends over time, and top products/customers.

# Hints:
# - Set up QuickSight permissions for S3 and Athena access.
# - Use QuickSight's drag-and-drop interface to create visualizations.
# - Example: Bar chart for sales by category, line chart for sales trends over time.
                      

# Set up AWS Resources:

# Create an S3 bucket.
# Create a DynamoDB table.
# Set up SNS and SES configurations.
# Ensure your Lambda function has proper permissions.
# Write Lambda Code:

# Start with S3 integration and gradually add DynamoDB, SNS, SES, and CloudWatch functionality.
# Follow the comments and hints provided to structure your function.


# Deploy and Test:

# Deploy the Lambda function and test by uploading files to the S3 bucket.
# Verify the file metadata is stored in DynamoDB, notifications are sent via SNS, and email reports are sent via SES.
# Monitor Logs:

# Check CloudWatch logs to ensure the function executed as expected.
# Identify and fix any issues logged in CloudWatch.

# - Set up QuickSight permissions for S3 and Athena access.
# - Use QuickSight's drag-and-drop interface to create visualizations.
# - Example: Bar chart for sales by category, line chart for sales trends over time.


# STEP BY STEP SUMMARY GUIDE:

# Part 1: Automate File Processing with Lambda

# Step 1: Set Up AWS Resources:

# S3 Bucket:
# Create an S3 bucket (e.g., my-file-processing-bucket).
# Enable event notifications for PutObject events (when a file is uploaded).
# Add a folder (optional) to organize uploaded files.

# DynamoDB Table:
# Create a table named FileMetadataTable.
# Primary key: FileName (String).
# Additional attributes: BucketName, ContentType, FileSize, and LastModified.

# SNS Topic:
# Create an SNS topic (e.g., FileUploadNotifications).
# Add at least one email subscriber to the topic.
# SES Configuration:

# Verify email addresses (sender and recipients) in SES if working in sandbox mode.

# IAM Role:
# Assign your Lambda function a role with the following permissions:
# s3:GetObject
# dynamodb:PutItem
# sns:Publish
# ses:SendEmail
# logs:CreateLogStream and logs:PutLogEvents for CloudWatch.
# Step 2: Write and Configure Lambda Function

# Function Workflow:
# Trigger Lambda when a file is uploaded to S3.
# Extract metadata about the file (e.g., name, size, content type).
# Store metadata in DynamoDB.
# Send an SNS notification about the file upload.
# Send a detailed email report using SES.
# Log all events in CloudWatch.


#Step 2: Implementation Steps:

# S3 Integration:
# Parse the event to retrieve bucket name and file details.
# Use the head_object API to get metadata.

# DynamoDB Integration:
# Store file metadata in the FileMetadataTable.

# SNS Integration:
# Publish a notification to the SNS topic with file details.

# SES Integration:
# Compose an email with file metadata and send it via SES.

# CloudWatch Integration:
# Add log statements for debugging and monitoring.


# Step 3: Deploy and Test:

# Deploy the Lambda function.
# Upload a file to the S3 bucket.
# Verify the following:
# File metadata is stored in DynamoDB.
# An SNS notification is sent to subscribers.
# An email report is received via SES.
# Logs are available in CloudWatch.


# Part 2: Query Data with Athena:

# Step 4: Configure Athena:

# Set Up an S3 Data Catalog:

# Configure Athena to query the S3 bucket where files are stored.
# Define the schema based on the file structure (e.g., CSV headers).
# Perform SQL Queries:

# Use queries to analyze the data, such as:
# sql
# Copy code
# SELECT Category, SUM(Total) AS TotalSales
# FROM sales_data_table
# GROUP BY Category;


# Step 5: Optimize for Real-Time Queries:

# Integrate AWS Glue for ETL tasks to prepare data for Athena.
# Store query results in an S3 bucket.


# Part 3: Visualize Data in QuickSight:

# Step 6: Connect QuickSight to Athena:

# Set up a new QuickSight data source linked to Athena.
# Build datasets based on Athena queries.


# Step 7: Create Dashboards
# Use the drag-and-drop interface to create:
# Bar charts for sales by category.
# Line charts for trends over time.
# Top 10 customers or products.
# Summary of Student Tasks


# Set Up Resources:

# S3 bucket, DynamoDB table, SNS topic, SES email configuration, and IAM role.
# Lambda Function:

# Implement integrations for S3, DynamoDB, SNS, SES, and CloudWatch.
# Athena Queries:

# Query data in the S3 bucket using SQL.
# QuickSight Dashboards:

# Visualize results from Athena queries.
# Validation
# Confirm metadata storage in DynamoDB.
# Check notifications and email reports.
# Run SQL queries and validate results.
# Ensure QuickSight dashboards visualize the required insights.

# SOLUTION:

# Complete Lambda function code that handles the file upload process, including storing metadata 
# in DynamoDB,sending SNS notifications, sending SES emails, and logging events to CloudWatch:

import json
import boto3
import logging
import time

# Initialize AWS services:

s3_client = boto3.client('s3')
dynamodb_client = boto3.client('dynamodb')
sns_client = boto3.client('sns')
ses_client = boto3.client('ses')
cloudwatch_client = boto3.client('logs')

# Log setup
logging.basicConfig(level=logging.INFO)

def lambda_handler(event, context):
    try:
        # Extract event details
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_name = event['Records'][0]['s3']['object']['key']
        
        # Step 2.2: Retrieve file metadata using head_object
        file_metadata = s3_client.head_object(Bucket=bucket_name, Key=file_name)
        
        # Extract relevant metadata
        content_type = file_metadata['ContentType']
        file_size = file_metadata['ContentLength']
        last_modified = file_metadata['LastModified'].strftime("%Y-%m-%d %H:%M:%S")
        
        # Step 2.3: Store metadata in DynamoDB
        dynamodb_client.put_item(
            TableName='FileMetadataTable',
            Item={
                'FileName': {'S': file_name},
                'BucketName': {'S': bucket_name},
                'ContentType': {'S': content_type},
                'FileSize': {'N': str(file_size)},
                'LastModified': {'S': last_modified}
            }
        )
        
        # Step 2.4: Publish SNS notification
        sns_message = f"New file uploaded: {file_name} in bucket {bucket_name}. Size: {file_size} bytes."
        sns_client.publish(
            TopicArn='arn:aws:sns:REGION:ACCOUNT_ID:FileUploadNotifications',
            Message=sns_message,
            Subject="File Upload Notification"
        )
        
        # Step 2.5: Send email report via SES
        email_subject = f"New File Uploaded: {file_name}"
        email_body = f"""
        A new file has been uploaded:
        File Name: {file_name}
        Bucket Name: {bucket_name}
        Content Type: {content_type}
        File Size: {file_size} bytes
        Last Modified: {last_modified}
        """
        ses_client.send_email(
            Source='sender@example.com',
            Destination={
                'ToAddresses': ['recipient@example.com']
            },
            Message={
                'Subject': {'Data': email_subject},
                'Body': {'Text': {'Data': email_body}}
            }
        )
        
        # Step 2.6: Log the event in CloudWatch
        logging.info(f"Successfully processed file: {file_name}")
        cloudwatch_client.put_log_events(
            logGroupName='FileProcessingLogGroup',
            logStreamName='FileProcessingStream',
            logEvents=[{
                'timestamp': int(time.time() * 1000),
                'message': f"Processed file {file_name} from bucket {bucket_name}"
            }]
        )

        return {
            'statusCode': 200,
            'body': json.dumps('File processed successfully')
        }

    except Exception as e:
        logging.error(f"Error processing file: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing file')
        }


# Explanation of the Code:

# The function is triggered by an S3 event (file upload).
# It retrieves the file metadata (e.g., content type, size, and last modified date) using the head_object API from S3.
# It stores the metadata in DynamoDB.
# It sends an SNS notification with the file upload details.
# It sends an email via SES with the same file details.
# It logs the event to CloudWatch for monitoring purposes.