
# Boto3 Documentation

# https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

# Install the boto3 library using pip:

    # pip install boto3

# Set up AWS credentials on your machine using the AWS CLI:

    #aws configure

# Exercise 1: Create and Manage S3 Buckets with Boto3 library.
# Objective: Teach students how to interact with Amazon S3 using Boto3 library.This includes:
    # Creating and managing S3 buckets.
    # Uploading files to and deleting files from an S3 bucket.
    # Handling exceptions when interacting with S3.
    # Using environment variables for AWS credentials to keep the credentials secure.
    
# Steps:
    # Setup AWS credentials using environment variables.
    # Create an S3 bucket and handle the exception if the bucket name already exists.
    # Upload a file to the bucket.
    # List all files in the bucket.
    # Delete a file from the bucket.
    # Delete the S3 bucket.

# Challenges:
    # Handle exceptions when creating a bucket with a name that already exists.
    # Use environment variables for AWS credentials.

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
import os

# Initialize the S3 client:

s3_client = boto3.client('s3')

# 1. Create an S3 bucket:

def create_s3_bucket(bucket_name):
    try:
        # Create the bucket
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' created successfully.")
    except s3_client.exceptions.BucketAlreadyExists as e:
        print(f"Bucket name '{bucket_name}' already exists. Try another unique name.")
    except s3_client.exceptions.BucketAlreadyOwnedByYou as e:
        print(f"Bucket '{bucket_name}' is already owned by your AWS account.")
    except NoCredentialsError:
        print("Credentials not available.")
    except PartialCredentialsError:
        print("Incomplete credentials provided.")
    except ClientError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unknown error occurred: {e}")

# 2. Upload a file to the bucket:

def upload_file_to_s3(bucket_name, file_path, object_name):
    try:
        # Upload the file
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File '{file_path}' uploaded to '{bucket_name}/{object_name}' successfully.")
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except NoCredentialsError:
        print("Credentials not available.")
    except PartialCredentialsError:
        print("Incomplete credentials provided.")
    except ClientError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unknown error occurred: {e}")


# 3. List all files in the bucket:

def list_files_in_s3(bucket_name):
    try:
        # List objects in the bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            print(f"Files in '{bucket_name}':")
            for obj in response['Contents']:
                print(obj['Key'])
        else:
            print(f"No files found in '{bucket_name}'.")
    except NoCredentialsError:
        print("Credentials not available.")
    except PartialCredentialsError:
        print("Incomplete credentials provided.")
    except ClientError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unknown error occurred: {e}")

# 4. Delete a file from the bucket:

def delete_file_from_s3(bucket_name, object_name):
    try:
        # Delete the file
        s3_client.delete_object(Bucket=bucket_name, Key=object_name)
        print(f"File '{object_name}' deleted from '{bucket_name}' successfully.")
    except NoCredentialsError:
        print("Credentials not available.")
    except PartialCredentialsError:
        print("Incomplete credentials provided.")
    except ClientError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unknown error occurred: {e}")

# 5. Delete the bucket:

def delete_s3_bucket(bucket_name):
    try:
        # Delete the bucket
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted successfully.")
    except NoCredentialsError:
        print("Credentials not available.")
    except PartialCredentialsError:
        print("Incomplete credentials provided.")
    except ClientError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unknown error occurred: {e}")


# Example usage:

if __name__ == "__main__":
    # Set the bucket name, file path, and object name as Variables
    # Bucket and file details:

    bucket_name = "shopsmartlytoday-bucket" 
    file_path = r"C:\Repositories\awsclass102024\Python_Code\sample.txt"  
    object_name = "uploaded_file.txt"  
    region = "us-east-1"

    # Check if the file exists locally, if not, create it
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write("This is a sample file content.")
        print(f"File '{file_path}' created.")

    # 1. Create the bucket
    create_s3_bucket(bucket_name)

    # 2. Upload the file to the bucket
    upload_file_to_s3(bucket_name, file_path, object_name)

    # 3. List files in the bucket
    list_files_in_s3(bucket_name)

    # 4. Delete the file from the bucket
    delete_file_from_s3(bucket_name, object_name)

    # 5. List files again to ensure the file was deleted
    list_files_in_s3(bucket_name)

    # 6. Delete the bucket
    delete_s3_bucket(bucket_name)



# Exercise 2: DynamoDB CRUD Operations
# Objective: Teach students how to interact with DynamoDB using Boto3.

# Steps:
# Create a DynamoDB table (e.g., Students with attributes StudentID and Name).
# Insert records into the table.
# Retrieve all records.
# Update a record in the table.
# Delete a record from the table.
# Challenges :
# Use the correct data types for attributes (e.g., string, number).
# Implement a function to query the table based on a specific StudentID.

# Step 1: Create a DynamoDB Table:
# First, in DynamoDB a table with StudentID as the partition key and Name as an attribute will be created.

import boto3

def create_table():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.create_table(
        TableName='Students',
        KeySchema=[
            {
                'AttributeName': 'StudentID',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'StudentID',
                'AttributeType': 'S'  # String data type for StudentID
            },
            {
                'AttributeName': 'Name',
                'AttributeType': 'S'  # String data type for Name
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    print("Table status:", table.table_status)

create_table()

# Step 2: Insert Records into the Table:
# Now that we have the table, let's insert records (students) into the table.

def insert_record(student_id, name):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Students')

    # Insert record into the table
    table.put_item(
        Item={
            'StudentID': student_id,
            'Name': name
        }
    )
    print(f"Inserted record for student {student_id}.")

# Example insert:
insert_record('S001', 'Alice')
insert_record('S002', 'Bob')
insert_record('S003', 'Charlie')

# Step 3: Retrieve All Records:
# Next, we’ll retrieve all records from the table. Note that DynamoDB does not have a direct “select *” operation, 
# so we use a scan operation to retrieve all items.

def get_all_records():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Students')

    # Scan the table to retrieve all records
    response = table.scan()
    items = response.get('Items', [])

    for item in items:
        print(f"StudentID: {item['StudentID']}, Name: {item['Name']}")

get_all_records()

# Step 4: Update a Record in the Table:
# To update a record, we will use the update_item method. For example, let’s change the name of the 
# student with StudentID 'S001' from "Alice" to "Alicia".

def update_record(student_id, new_name):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Students')

    # Update the record with the new name
    table.update_item(
        Key={
            'StudentID': student_id
        },
        UpdateExpression='SET Name = :new_name',
        ExpressionAttributeValues={
            ':new_name': new_name
        }
    )
    print(f"Updated StudentID {student_id} to name {new_name}.")

update_record('S001', 'Alicia')


# Step 5: Delete a Record from the Table:
# We can delete a record from the table using the delete_item method. Let’s delete the student with StudentID 'S003'.

def delete_record(student_id):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Students')

    # Delete the record from the table
    table.delete_item(
        Key={
            'StudentID': student_id
        }
    )
    print(f"Deleted record for student {student_id}.")

delete_record('S003')


# Step 6: Query a Record Based on StudentID:
# Finally, we need to implement a function to query the table for a specific StudentID and retrieve the associated Name.

def query_record(student_id):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Students')

    # Query the table based on StudentID
    response = table.get_item(
        Key={
            'StudentID': student_id
        }
    )

    item = response.get('Item')
    if item:
        print(f"StudentID: {item['StudentID']}, Name: {item['Name']}")
    else:
        print(f"No record found for StudentID {student_id}")

query_record('S001')
query_record('S999')  # Example of a non-existent StudentID

# Putting It All Together:
# We can now run these functions in sequence to:

# Create the DynamoDB table.
# Insert records.
# Retrieve all records.
# Update records.
# Delete records.
# Query records based on StudentID.

# Challenges:
# Ensure you're using the correct data types when inserting records. For example, StudentID is a string, and Name is also a string.
# Handle edge cases where records might not exist when querying or deleting items.
# Adjust the read and write capacity units in case you expect higher traffic, or consider using on-demand mode.
# This approach gives us a comprehensive guide to working with DynamoDB in Python using Boto3, covering all basic CRUD operations.


# Exercise 3: EC2 Instance Management
# Objective: Teach students how to launch and manage EC2 instances using Boto3.

# Steps:
# Launch an EC2 instance.
# Retrieve the public IP address of the instance.
# Stop the instance.
# Start the instance again.
# Terminate the instance.

# Challenges:
# Use tags to name the instance.
# Create a security group and associate it with the instance.
# Handle errors when attempting to start/stop an already running/stopped instance.


# Step-by-Step Implementation:

# Step 1: Launch an EC2 Instance

# Let's start by launching an EC2 instance with a tag and security group.


import boto3
from botocore.exceptions import ClientError

def create_security_group():
    ec2 = boto3.client('ec2', region_name='us-east-1')

    try:
        # Create a security group:
        response = ec2.create_security_group(
            GroupName='shopsmartlytoday-sg',
            Description='Security group for EC2 instance'
        )
        security_group_id = response['GroupId']

        # Add inbound rule to allow SSH access:
        ec2.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 22,
                    'ToPort': 22,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]  # Allow SSH from anywhere
                }
            ]
        )

        print(f"Security group created with ID: {security_group_id}")
        return security_group_id
    except ClientError as e:
        print(f"Error creating security group: {e}")
        return None

def launch_ec2_instance(security_group_id):
    ec2 = boto3.resource('ec2', region_name='us-east-1')

    # Launch an EC2 instance:
    instance = ec2.create_instances(
        ImageId='ami-01e3c4a339a264cc9',  # Use an appropriate AMI ID
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',  # Choose an appropriate instance type
        SecurityGroupIds=[security_group_id],
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'shopsmartlytoday-ec2'}]
        }]
    )

    instance_id = instance[0].id
    print(f"EC2 Instance launched with ID: {instance_id}")
    return instance_id

# Create security group and launch instance
security_group_id = create_security_group()
if security_group_id:
    instance_id = launch_ec2_instance(security_group_id)

# In this example:
# We create a security group and allow inbound SSH traffic (port 22).
# Then, we launch an EC2 instance with a specific AMI ID, instance type, and attach the security group to the instance.
# We also tag the instance with a name, shopsmartlytoday-ec2.

# Step 2: Retrieve the Public IP Address of the Instance:

# Once the instance is launched, we can fetch its public IP address.

def get_public_ip(instance_id):
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    instance = ec2.Instance(instance_id)

    # Wait until the instance is running:
    instance.wait_until_running()

    # Retrieve the public IP address:
    public_ip = instance.public_ip_address
    print(f"Public IP address of instance {instance_id}: {public_ip}")
    return public_ip

# Fetch the public IP address of the instance:
get_public_ip(instance_id)

# This function waits for the instance to be in the running state and then retrieves the public IP.

# Step 3: Stop the EC2 Instance:

# To stop an EC2 instance, use the stop() method.

def stop_instance(instance_id):
    ec2 = boto3.client('ec2', region_name='us-east-1')

    try:
        # Stop the instance
        ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} stopped.")
    except ClientError as e:
        print(f"Error stopping instance {instance_id}: {e}")

# Stop the EC2 instance
stop_instance(instance_id)

# This will stop the EC2 instance and handle errors in case the instance is already stopped.

# Step 4: Start the EC2 Instance
# To start an EC2 instance, use the start() method.

def start_instance(instance_id):
    ec2 = boto3.client('ec2', region_name='us-east-1')

    try:
        # Start the instance
        ec2.start_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} started.")
    except ClientError as e:
        print(f"Error starting instance {instance_id}: {e}")

# Start the EC2 instance again
start_instance(instance_id)

# This will start the instance again and handle errors in case the instance is already running.


# Step 5: Terminate the EC2 Instance:

# Finally, to terminate the instance, we use the terminate() method.

def terminate_instance(instance_id):
    ec2 = boto3.client('ec2', region_name='us-east-1')

    try:
        # Terminate the instance
        ec2.terminate_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} terminated.")
    except ClientError as e:
        print(f"Error terminating instance {instance_id}: {e}")

# Terminate the EC2 instance
terminate_instance(instance_id)

# This will terminate the EC2 instance

# Error Handling:

# As mentioned in the steps above, we are using the ClientError exception from Boto3 to handle common errors:

# When starting an instance that is already running.
# When stopping an instance that is already stopped.
# When trying to terminate an already terminated instance.

# Putting It All Together
# Here’s a full implementation that manages an EC2 instance:

import boto3
from botocore.exceptions import ClientError

def create_security_group():
    ec2 = boto3.client('ec2', region_name='us-east-1')
    try:
        response = ec2.create_security_group(
            GroupName='shopsmartlytoday-sg',
            Description='Security group for EC2 instance'
        )
        security_group_id = response['GroupId']
        ec2.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[{
                'IpProtocol': 'tcp',
                'FromPort': 22,
                'ToPort': 22,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
            }]
        )
        return security_group_id
    except ClientError as e:
        print(f"Error: {e}")
        return None

def launch_ec2_instance(security_group_id):
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    instance = ec2.create_instances(
        ImageId='ami-01e3c4a339a264cc9',  
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        SecurityGroupIds=[security_group_id],
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'shopsmartlytoday-ec2'}]
        }]
    )
    return instance[0].id

def get_public_ip(instance_id):
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    instance = ec2.Instance(instance_id)
    instance.wait_until_running()
    return instance.public_ip_address

def stop_instance(instance_id):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    try:
        ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Stopped instance {instance_id}")
    except ClientError as e:
        print(f"Error stopping instance {instance_id}: {e}")

def start_instance(instance_id):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    try:
        ec2.start_instances(InstanceIds=[instance_id])
        print(f"Started instance {instance_id}")
    except ClientError as e:
        print(f"Error starting instance {instance_id}: {e}")

def terminate_instance(instance_id):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    try:
        ec2.terminate_instances(InstanceIds=[instance_id])
        print(f"Terminated instance {instance_id}")
    except ClientError as e:
        print(f"Error terminating instance {instance_id}: {e}")

# Example usage:

security_group_id = create_security_group()
instance_id = launch_ec2_instance(security_group_id)
public_ip = get_public_ip(instance_id)
print(f"Public IP: {public_ip}")
stop_instance(instance_id)
start_instance(instance_id)
terminate_instance(instance_id)



# Exercise 4: Lambda Function Deployment
# Objective: Teach students how to deploy and invoke an AWS Lambda function using Boto3.

# Steps:
# Create a Lambda function using an existing zip file.
# Add an execution role to the Lambda function.
# Invoke the Lambda function and display the response.
# Update the Lambda function code.
# Delete the Lambda function.
# Challenges :

# Use IAM to create a role programmatically for Lambda.
# Handle versioning when updating the function.

# To deploy, invoke, and manage AWS Lambda functions programmatically with Boto3, you can follow these steps. Below is a detailed guide that covers:

# Creating a Lambda function using an existing ZIP file.
# Adding an execution role for Lambda.
# Invoking the Lambda function and displaying the response.
# Updating the Lambda function code.
# Deleting the Lambda function.
# Creating an IAM role programmatically for Lambda.
# Handling versioning when updating the function.
# Pre-requisites:
# AWS account with appropriate IAM permissions (Lambda, IAM, and EC2 roles).
# Python 3.x installed and boto3 library installed (pip install boto3).
# A ZIP file containing your Lambda function code (e.g., lambda_function.zip).
# The boto3 SDK and IAM permissions to interact with AWS services.


# Step 1: Set up IAM Role for Lambda Function:

# Lambda functions need an execution role that allows them to access other AWS services 
# (e.g., S3, DynamoDB, etc.). Here’s how we can create an IAM role programmatically:

import boto3
from botocore.exceptions import ClientError

def create_lambda_execution_role():
    iam_client = boto3.client('iam')
    
    role_name = "LambdaExecutionRole"
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"Service": "lambda.amazonaws.com"},
                "Action": "sts:AssumeRole"
            }
        ]
    }
    
    try:
        # Create the role
        response = iam_client.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_policy),
            Description="Execution role for AWS Lambda"
        )
        
        # Attach the AWS managed policy for Lambda execution permissions (e.g., AWSLambdaBasicExecutionRole)
        iam_client.attach_role_policy(
            RoleName=role_name,
            PolicyArn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
        )
        
        print(f"Role created: {role_name}")
        return response['Role']['Arn']
    
    except ClientError as e:
        print(f"Error creating role: {e}")
        return None

role_arn = create_lambda_execution_role()

# Step 2: Create Lambda Function:

# Once the role is created, we can create a Lambda function using an existing ZIP file (lambda_function.zip) 
# that contains our Lambda function code.

import boto3
import json

def create_lambda_function(role_arn, zip_file_path):
    lambda_client = boto3.client('lambda')

    with open(zip_file_path, 'rb') as f:
        zip_data = f.read()

    function_name = 'MyLambdaFunction'

    try:
        response = lambda_client.create_function(
            FunctionName=function_name,
            Runtime='python3.8',  # Adjust according to your function code
            Role=role_arn,
            Handler='lambda_function.lambda_handler',  # Adjust this according to your function
            Code={'ZipFile': zip_data},
            Description='Test Lambda function',
            Timeout=10,
            MemorySize=128
        )
        
        print(f"Lambda function created: {response['FunctionName']}")
        return response['FunctionArn']
    
    except ClientError as e:
        print(f"Error creating Lambda function: {e}")
        return None

lambda_function_arn = create_lambda_function(role_arn, 'lambda_function.zip')

# Step 3: Invoke the Lambda Function:

# After deploying your Lambda function, you can invoke it programmatically and display the response.

def invoke_lambda_function(function_name):
    lambda_client = boto3.client('lambda')

    try:
        response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',  # Use 'Event' for asynchronous invocation
            Payload=json.dumps({'key1': 'value1'})  # Pass input data if needed
        )

        response_payload = json.loads(response['Payload'].read().decode())
        print(f"Lambda response: {response_payload}")
    
    except ClientError as e:
        print(f"Error invoking Lambda function: {e}")

invoke_lambda_function('MyLambdaFunction')


# Step 4: Update Lambda Function Code:

# Lambda functions support versioning. You can update the function code and deploy a new version.

def update_lambda_function(zip_file_path, function_name):
    lambda_client = boto3.client('lambda')

    with open(zip_file_path, 'rb') as f:
        zip_data = f.read()

    try:
        response = lambda_client.update_function_code(
            FunctionName=function_name,
            ZipFile=zip_data
        )

        print(f"Lambda function updated: {response['FunctionName']}")
        return response['Version']
    
    except ClientError as e:
        print(f"Error updating Lambda function: {e}")
        return None

updated_version = update_lambda_function('lambda_function_updated.zip', 'MyLambdaFunction')


# Step 5: Delete the Lambda Function:

# If you want to delete the Lambda function after testing, use the following code.

def delete_lambda_function(function_name):
    lambda_client = boto3.client('lambda')

    try:
        lambda_client.delete_function(
            FunctionName=function_name
        )
        print(f"Lambda function deleted: {function_name}")
    
    except ClientError as e:
        print(f"Error deleting Lambda function: {e}")

delete_lambda_function('MyLambdaFunction')


# Step 6: Managing Versions (Lambda Versioning):

# Lambda function versions allow us to maintain different versions of our function. When we 
# update the function, AWS Lambda creates a new version. Here's how to create and manage versions:

# Publish a version of the Lambda function after updating the code:

def publish_lambda_version(function_name):
    lambda_client = boto3.client('lambda')

    try:
        response = lambda_client.publish_version(
            FunctionName=function_name
        )
        
        print(f"Lambda version published: {response['Version']}")
        return response['Version']
    
    except ClientError as e:
        print(f"Error publishing Lambda version: {e}")
        return None

version = publish_lambda_version('MyLambdaFunction')

# Conclusion:
# These steps provide a comprehensive process to deploy, invoke, update, and manage AWS Lambda functions 
# programmatically using Boto3. 
# Additionally, versioning and IAM role management are handled to ensure secure and efficient execution of the Lambda function.
# This guide will help you handle Lambda function deployments in real-world scenarios, including managing execution roles, 
# invoking functions, and updating code in a version-controlled manner.


# Exercise 5: CloudWatch Logs and Monitoring
# Objective: Teach students how to use CloudWatch for logging and monitoring resources.

# Steps:
# Create a log group and log stream.
# Write a custom log entry to the stream.
# Retrieve log events from the stream.
# Set up a metric filter on the log group.
# Delete the log group.
# Challenges :

# Create and use IAM policies that allow access to CloudWatch.
# Parse log data to find specific patterns (e.g., errors or warnings).


# To help students understand how to use AWS CloudWatch for logging and monitoring resources, the following
# steps outline how to interact with CloudWatch Logs, manage log groups and streams, write custom log 
# entries, retrieve logs, set up metric filters, and clean up resources. Additionally, we will cover 
# IAM policy creation and parsing log data for patterns.

# Pre-requisites:
# AWS account with permissions to access CloudWatch, IAM, and the necessary resources.
# boto3 installed (pip install boto3).

# Step 1: Create a Log Group and Log Stream:

# To begin working with AWS CloudWatch Logs, we first need to create a Log Group and a Log Stream within 
# that group.


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

# Step 2: Write a Custom Log Entry to the Stream:

# Once the log stream is created, we can add custom log entries. 
# The following code demonstrates how to write a log event to the stream.


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

# To view the logs in our stream, we can retrieve the log events. 
# This can be helpful for monitoring, troubleshooting, or analyzing your logs.


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

# Step 4: Set up a Metric Filter on the Log Group:

# CloudWatch allows you to create metric filters that can trigger alarms or create custom CloudWatch 
# metrics based on log events. Here's an example of setting up a metric filter that counts occurrences 
# of the word "ERROR" in the logs:


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

# We can now track how many times the word "ERROR" appears in the logs and create CloudWatch alarms 
# based on this metric.

# Step 5: Delete the Log Group:

# Once we no longer need the log group and its streams, we can delete them:


def delete_log_group(log_group_name):
    logs_client = boto3.client('logs')

    try:
        logs_client.delete_log_group(logGroupName=log_group_name)
        print(f"Log group '{log_group_name}' deleted.")
    
    except ClientError as e:
        print(f"Error deleting log group: {e}")

delete_log_group(log_group)

# Challenges:
# 1. Create and use IAM Policies that Allow Access to CloudWatch
# To allow our Lambda function (or any IAM user) to interact with CloudWatch, we need to create an IAM 
# policy with appropriate permissions. Below is an example of an IAM policy that grants permissions for 
# CloudWatch Logs.

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

# We can attach this policy to the IAM role or user interacting with CloudWatch Logs to grant access.

# 2. Parse Log Data to Find Specific Patterns (e.g., errors or warnings)

# We can search the log data for patterns such as "ERROR" or "WARNING" by scanning the logs 
# and filtering the messages. Here's an example of parsing logs to find errors:


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

# In this case, the script uses regular expressions to find log entries containing "ERROR" 
# and prints them out.

Conclusion:

# This exercise teaches students how to interact with CloudWatch Logs for logging and monitoring:

# Creating log groups and streams.
# Writing and retrieving log entries.
# Setting up metric filters for tracking specific log patterns.
# Deleting log groups when no longer needed.
# Handling IAM policies and parsing logs for specific events.
# Students will also get hands-on experience parsing log data and creating 
# CloudWatch metrics to set up monitoring solutions for AWS resources.



