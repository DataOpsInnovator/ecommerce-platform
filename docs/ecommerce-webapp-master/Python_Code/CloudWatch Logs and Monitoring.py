
# AWS CloudWatch Logs and Monitoring are essential for tracking, storing, and analyzing logs from 
# our AWS resources and applications. We can use CloudWatch Logs to monitor, store, and access logs, 
# and we can use CloudWatch Metrics and Alarms to monitor resource performance, set thresholds, and 
# automate actions when certain conditions are met.

# Key Features of CloudWatch Logs:

# 1. Log Groups and Log Streams:

    # Log Group: A container for logs from different sources.
    # Log Stream: A sequence of log events from the same source (e.g., EC2 instance or Lambda function).
# 2. Log Events: Individual entries in a log stream that contain timestamped data (such as messages from 
#    an application or a system).

# 3. Metric Filters: Extract useful metrics from logs and create custom CloudWatch metrics.

# 4. CloudWatch Alarms: Set up alarms based on the metrics you collect, which can trigger notifications 
#     or automated actions.

# Step-by-Step Guide to Working with CloudWatch Logs and Monitoring:

# Let’s break down how to work with CloudWatch Logs and how to set up monitoring and alarms.

# Step 1: Create a Log Group and Log Stream:

# A Log Group is a collection of log streams that share the same retention, monitoring, and access control
# settings. You can create a log group and stream using AWS SDK (like Boto3 for Python).

import boto3
from botocore.exceptions import ClientError

def create_log_group_and_stream(log_group_name, log_stream_name):
    logs_client = boto3.client('logs')

    try:
        # Create log group if it doesn't exist
        logs_client.create_log_group(logGroupName=log_group_name)
        print(f"Log group '{log_group_name}' created.")

    except ClientError as e:
        print(f"Log group '{log_group_name}' already exists or error: {e}")

    try:
        # Create log stream within the log group
        logs_client.create_log_stream(
            logGroupName=log_group_name,
            logStreamName=log_stream_name
        )
        print(f"Log stream '{log_stream_name}' created.")
    except ClientError as e:
        print(f"Error creating log stream: {e}")

log_group = "MyLogGroup"
log_stream = "MyLogStream"
create_log_group_and_stream(log_group, log_stream)


# Step 2: Write Custom Log Entries:

# Once the log group and stream are created, we can send log entries (events) to the stream. 
# These log events can contain any type of information such as application logs, error messages, 
# or other details.


import time

def write_log_entry(log_group_name, log_stream_name, message):
    logs_client = boto3.client('logs')

    # Get the sequence token for the log stream (used for sequential log events)
    try:
        response = logs_client.describe_log_streams(
            logGroupName=log_group_name,
            logStreamNamePrefix=log_stream_name
        )
        
        # Get the sequence token (for subsequent log events)
        sequence_token = response['logStreams'][0].get('uploadSequenceToken')
        
        # Put log event with a timestamp
        log_event = {
            'logGroupName': log_group_name,
            'logStreamName': log_stream_name,
            'logEvents': [
                {
                    'timestamp': int(time.time() * 1000),  # Current time in milliseconds
                    'message': message
                }
            ]
        }

        if sequence_token:
            log_event['sequenceToken'] = sequence_token

        logs_client.put_log_events(**log_event)
        print(f"Log entry written: {message}")

    except ClientError as e:
        print(f"Error writing log entry: {e}")

write_log_entry(log_group, log_stream, "This is a custom log entry")


# Step 3: Retrieve Log Events from the Stream:

# We can retrieve log events from a log stream to view the logs and analyze them.

def retrieve_log_events(log_group_name, log_stream_name):
    logs_client = boto3.client('logs')

    try:
        response = logs_client.get_log_events(
            logGroupName=log_group_name,
            logStreamName=log_stream_name,
            startFromHead=True  # Retrieve logs from the beginning
        )

        for event in response['events']:
            print(f"Log Event: {event['message']} at {event['timestamp']}")

    except ClientError as e:
        print(f"Error retrieving log events: {e}")

retrieve_log_events(log_group, log_stream)


# Step 4: Set up Metric Filter on Log Group:

# CloudWatch allows us to create metric filters to track certain patterns in our logs, 
# such as the occurrence of specific keywords (e.g., "ERROR", "WARN").

# Here’s an example that sets up a metric filter for counting occurrences of "ERROR":


def create_metric_filter(log_group_name, filter_name):
    logs_client = boto3.client('logs')

    filter_pattern = "ERROR"  # Look for logs containing "ERROR"

    try:
        response = logs_client.put_metric_filter(
            logGroupName=log_group_name,
            filterName=filter_name,
            filterPattern=filter_pattern,
            metricTransformations=[
                {
                    'metricName': 'ErrorCount',
                    'metricNamespace': 'MyNamespace',
                    'metricValue': '1'
                }
            ]
        )
        print(f"Metric filter '{filter_name}' created with pattern '{filter_pattern}'.")

    except ClientError as e:
        print(f"Error creating metric filter: {e}")

create_metric_filter(log_group, "ErrorFilter")


# Step 5: Create a CloudWatch Alarm Based on the Metric:

# Once we have created a metric filter,we can set up a CloudWatch Alarm that triggers based on the metric’s 
# value (e.g., when the number of errors exceeds a threshold).


def create_alarm():
    cloudwatch_client = boto3.client('cloudwatch')

    try:
        response = cloudwatch_client.put_metric_alarm(
            AlarmName='HighErrorCount',
            MetricName='ErrorCount',
            Namespace='MyNamespace',
            Statistic='Sum',
            Period=60,  # 1-minute period
            EvaluationPeriods=1,
            Threshold=5,  # Trigger if more than 5 errors are logged
            ComparisonOperator='GreaterThanThreshold',
            AlarmActions=['arn:aws:sns:region:account-id:sns-topic']  # Replace with SNS ARN for notification
        )
        print("CloudWatch alarm created: HighErrorCount")

    except ClientError as e:
        print(f"Error creating alarm: {e}")

create_alarm()

# This alarm will trigger if the ErrorCount metric exceeds 5 within a 1-minute period.

# Step 6: Delete the Log Group:

# Once we are done with the log group and its streams, we can delete them to avoid 
# unnecessary storage costs.


def delete_log_group(log_group_name):
    logs_client = boto3.client('logs')

    try:
        logs_client.delete_log_group(logGroupName=log_group_name)
        print(f"Log group '{log_group_name}' deleted.")
    
    except ClientError as e:
        print(f"Error deleting log group: {e}")

delete_log_group(log_group)

# Challenges:

# 1. Create and Use IAM Policies for CloudWatch Access
# To allow programmatic access to CloudWatch Logs, we must create an IAM policy. 
# Here's an example IAM policy granting necessary permissions for logging:


{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "logs:GetLogEvents",
                "logs:DescribeLogStreams",
                "logs:PutMetricFilter",
                "logs:DeleteLogGroup"
            ],
            "Resource": "*"
        }
    ]
}

# We can attach this policy to an IAM role that your Lambda functions or 
# EC2 instances use to interact with CloudWatch.

# 2. Parse Log Data for Specific Patterns (Errors or Warnings):
    
# We can parse log data to identify patterns (e.g., errors or warnings) using regular expressions 
# (regex) or other techniques. Here's how you can identify errors in log entries:


import re

def parse_logs_for_errors(log_group_name, log_stream_name):
    logs_client = boto3.client('logs')

    try:
        response = logs_client.get_log_events(
            logGroupName=log_group_name,
            logStreamName=log_stream_name,
            startFromHead=True
        )

        for event in response['events']:
            message = event['message']
            if re.search(r'ERROR', message):  # Find logs with 'ERROR'
                print(f"Error found: {message}")

    except ClientError as e:
        print(f"Error parsing logs: {e}")

parse_logs_for_errors(log_group, log_stream)

# This code parses through the logs and identifies any log entries that contain the word "ERROR".

# Conclusion:

# With CloudWatch Logs and Monitoring, we can:

# Track log events and errors from your resources.
# Create metric filters to extract useful metrics.
# Set up CloudWatch Alarms to monitor resource performance and trigger automated actions.
# Use IAM policies to control access to CloudWatch.
# These capabilities provide a powerful way to monitor and respond to events across your AWS environment.