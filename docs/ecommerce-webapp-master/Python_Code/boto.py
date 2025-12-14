# pip install boto3
# aws configure

import boto3
import os

# Create an S3 client
s3 = boto3.client('s3')

# Bucket and file details
bucket_name = "my-demo-bucket-exercise"
file_name = "example.txt"
download_file_name = "downloaded_example.txt"
region = "us-east-1"
content = "dssomsdofadog dsgdsgdsajgl dpogj pdgjpoadsjgpoasdugeqowg posdaug aposdjg adsgjas;djgpuew0e4 j"

def create_bucket(bucket_name):
    """Create an S3 bucket."""
    try:
        s3.create_bucket(
            Bucket=bucket_name,
            #CreateBucketConfiguration={'LocationConstraint': region}
        )
        print(f"Bucket '{bucket_name}' created successfully!")
    except Exception as e:
        print(f"Error creating bucket: {e}")


def upload_file(bucket_name, file_name):
    """Upload a file to the S3 bucket."""
    with open(file_name, "w") as f:
        f.write("This is a demo file for the Boto3 exercise.")
    
    try:
        s3.upload_file(file_name, bucket_name, file_name)
        print(f"File '{file_name}' uploaded successfully to bucket '{bucket_name}'!")
    except Exception as e:
        print(f"Error uploading file: {e}")

def list_files(bucket_name):
    """List all files in the S3 bucket."""
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            print("Files in bucket:")
            for obj in response['Contents']:
                print(f" - {obj['Key']}")
        else:
            print("No files found in bucket.")
    except Exception as e:
        print(f"Error listing files: {e}")

# def download_file(bucket_name, file_name, download_file_name):
#     """Download a file from the S3 bucket."""
#     try:
#         s3.download_file(bucket_name, file_name, download_file_name)
#         print(f"File '{file_name}' downloaded successfully as '{download_file_name}'!")
#     except Exception as e:
#         print(f"Error downloading file: {e}")

# def delete_file(bucket_name, file_name):
#     """Delete a file from the S3 bucket."""
#     try:
#         s3.delete_object(Bucket=bucket_name, Key=file_name)
#         print(f"File '{file_name}' deleted successfully from bucket '{bucket_name}'!")
#     except Exception as e:
#         print(f"Error deleting file: {e}")

# def delete_bucket(bucket_name):
#     """Delete an S3 bucket."""
#     try:
#         s3.delete_bucket(Bucket=bucket_name)
#         print(f"Bucket '{bucket_name}' deleted successfully!")
#     except Exception as e:
#         print(f"Error deleting bucket: {e}")

# Workflow execution
if __name__ == "__main__":
    create_bucket(bucket_name)
    upload_file(bucket_name, file_name)
    # list_files(bucket_name)
    # download_file(bucket_name, file_name, download_file_name)
    # delete_file(bucket_name, file_name)
    # delete_bucket(bucket_name)

    # # Clean up local file
    # os.remove(file_name)
    # os.remove(download_file_name)


# Here's an explanation of each line of the Python script provided:

# Preparation Steps:

# Commented Out Commands:

    # pip install boto3
    # aws configure

# These are commented out as they are terminal commands, not Python code.

# pip install boto3 installs the boto3 library, which is the AWS SDK for Python, enabling interaction with AWS services like S3.
    
# aws configure sets up the AWS CLI (Command Line Interface) with access keys and default region, allowing Boto3 to authenticate AWS requests.

# Imports and Client Setup:

# Importing libraries:

    import boto3
    import os

# boto3: This library is the AWS SDK for Python, which is used to interact with various AWS services, including S3 (Simple Storage Service).
# os: This is a built-in Python library used for interacting with the operating system. It's used here to remove local files later in the script.


# Create an S3 client:

    s3 = boto3.client('s3')

# boto3.client('s3') creates a low-level client object for Amazon S3. This object is used to interact with S3 services, such as creating buckets, uploading, listing, and downloading files.

# Bucket and File Details:

# Bucket and file information:


    bucket_name = "my-demo-bucket-exercise"
    file_name = "example.txt"
    download_file_name = "downloaded_example.txt"
    region = "us-east-1"
    content = "dssomsdofadog dsgdsgdsajgl dpogj pdgjpoadsjgpoasdugeqowg posdaug aposdjg adsgjas;djgpuew0e4 j"


# bucket_name: The name of the S3 bucket that will be used. This name must be globally unique.

# file_name: The name of the file to upload to the S3 bucket. This file will be created locally and uploaded.

# download_file_name: The name used to save the file when downloading it from the S3 bucket.

# region: The AWS region in which the bucket will be created.

# content: A string that could be used as file content, but it's not directly used in this script (the file will contain a demo message).

# Function Definitions:

# Create Bucket
# Create a new S3 bucket:

    def create_bucket(bucket_name):
        """Create an S3 bucket."""
        try:
            s3.create_bucket(Bucket=bucket_name)
            print(f"Bucket '{bucket_name}' created successfully!")
        except Exception as e:
            print(f"Error creating bucket: {e}")
    create_bucket(bucket_name)                        # This function attempts to create an S3 bucket with the given bucket_name. 
                                                      # If successful, it prints a success message; otherwise, it prints an error message.

# Upload File
# Upload a file to the S3 bucket:

    def upload_file(bucket_name, file_name):
        """Upload a file to the S3 bucket."""
        with open(file_name, "w") as f:
            f.write("This is a demo file for the Boto3 exercise.")
        try:
            s3.upload_file(file_name, bucket_name, file_name)
            print(f"File '{file_name}' uploaded successfully to bucket '{bucket_name}'!")
        except Exception as e:
            print(f"Error uploading file: {e}")
    upload_file(bucket_name, file_name)         # This function writes content to a local file (file_name) and then uploads it to the specified S3 bucket.

# The file is first opened for writing (with open(file_name, "w") as f), and a demo message is written to it.
# Then, s3.upload_file() uploads the file to S3. If successful, it prints a success message.

# List Files in Bucket
# List files in the S3 bucket:


    def list_files(bucket_name):
        """List all files in the S3 bucket."""
        try:
            response = s3.list_objects_v2(Bucket=bucket_name)
            if 'Contents' in response:
                print("Files in bucket:")
                for obj in response['Contents']:
                    print(f" - {obj['Key']}")
            else:
                print("No files found in bucket.")
        except Exception as e:
            print(f"Error listing files: {e}")
    list_files(bucket_name)                      #This function lists all files in the specified S3 bucket.


# It calls s3.list_objects_v2() to retrieve the objects in the bucket. If there are files (i.e., 'Contents' exists in the response), it lists their names (obj['Key']).
# If no files are found, it prints "No files found in bucket."


# Download File:
# Download file from S3:


def download_file(bucket_name, file_name, download_file_name):
    """Download a file from the S3 bucket."""
    try:
        s3.download_file(bucket_name, file_name, download_file_name)
        print(f"File '{file_name}' downloaded successfully as '{download_file_name}'!")
    except Exception as e:
        print(f"Error downloading file: {e}")


# This function downloads the file from the specified S3 bucket and save it locally under download_file_name.


# Delete File:
# Delete a file from the S3 bucket:

def delete_file(bucket_name, file_name):
    """Delete a file from the S3 bucket."""
    try:
        s3.delete_object(Bucket=bucket_name, Key=file_name)
        print(f"File '{file_name}' deleted successfully from bucket '{bucket_name}'!")
    except Exception as e:
        print(f"Error deleting file: {e}")

# This deletes a file from the specified S3 bucket using s3.delete_object().



# Delete Bucket:
# Delete the S3 bucket:

def delete_bucket(bucket_name):
    """Delete an S3 bucket."""
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted successfully!")
    except Exception as e:
        print(f"Error deleting bucket: {e}")

# This deletes the specified S3 bucket using s3.delete_bucket().


# Main Workflow Execution:
# Main block:

    if __name__ == "__main__":
        create_bucket(bucket_name)
        upload_file(bucket_name, file_name)


list_files(bucket_name)
download_file(bucket_name, file_name, download_file_name)
delete_file(bucket_name, file_name)
delete_bucket(bucket_name)

# Clean up local file:

os.remove(file_name)
os.remove(download_file_name)

# This block is executed when the script is run directly.
# First, it calls create_bucket() to create the S3 bucket.
# Then, it calls upload_file() to upload a file to the bucket.
# The commented-out lines could be used to list files, download a file, delete a file, or delete the bucket, but they are not part of the current execution flow.
# After the file operations, it cleans up the local file (file_name) by calling os.remove() to delete it.

# Summary of Functional Steps:

# Creates a bucket in S3.
# Creates a local file and uploads it to that bucket.
# (Optionally) lists files, downloads, deletes files, and deletes the bucket (if uncommented).
# Cleans up local files after the operations are complete.


