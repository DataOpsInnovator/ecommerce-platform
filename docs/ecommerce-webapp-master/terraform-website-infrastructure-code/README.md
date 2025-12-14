<<<<<<< HEAD
# webapp

# Requirements

# INSTALL
1. https://www.terraform.io/
2. https://registry.terraform.io/
3. https://code.visualstudio.com/download
   
# TERRAFORM Documentation
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

# AWS ACCESS CONFIGURE COMAND
## aws configure

# TERRAFORM COMMANDS 
1. terraform init
2. terraform plan
3. terraform apply
=======
						Terraform Infrastructure Deployment for a Website

Overview:

This project deploys a complete, scalable infrastructure on AWS using Terraform. It creates a VPC, subnets, EC2 instances, security groups, and an Nginx web server to host a static website. Additionally, it includes a DNS configuration using AWS Route 53. This setup is designed to provide a highly available and secure environment for hosting a simple website with separate index.html, about.html, and contact.html pages.

The website infrastructure is managed entirely through Terraform, ensuring a reproducible, version-controlled deployment process. The web server is configured with Nginx and pre-configured HTML files.

Components:

AWS VPC: A virtual private cloud with public and private subnets.
EC2 Instance: An instance running Nginx to serve the static website.
Security Groups: To secure access to the EC2 instance (HTTP and SSH).
Route 53: DNS management for the domain name of the website.
User Data Script: A bash script that installs Nginx and sets up the website files automatically when the EC2 instance is launched.

Architecture Overview:

VPC: A custom VPC is created with CIDR block 10.0.0.0/16, providing private and public subnets.
Subnets: Two subnets, one public (10.0.1.0/24) and one private (10.0.2.0/24), are created in the us-east-1a availability zone.
EC2 Instance: The EC2 instance runs Nginx and serves the static files from /var/www/mywebsite/. The website is composed of simple HTML files that are pre-copied to the instance during initialization.
Security Groups: Security groups are configured to allow incoming traffic on ports 80 (HTTP) and 22 (SSH), restricted by the user's IP for SSH.
Route 53: DNS records point to the EC2 instance's public IP to enable access via a custom domain name (e.g., www.example.com).

Prerequisites:

Before you begin, ensure you have the following:

Terraform: Install Terraform if you don't already have it.
AWS Account: An active AWS account with access credentials (AWS Access Key and Secret Key).
SSH Key Pair: A valid SSH key pair to access the EC2 instance. Ensure the key is added to AWS EC2 (in the AWS Management Console or AWS CLI) before running the deployment.
Directory Structure

The project directory is structured as follows:

terraform-website-infrastructure/
├── modules/
│   ├── vpc/
│   │   └── main.tf              # VPC and subnet configurations
│   ├── ec2/
│   │   └── main.tf              # EC2 instance configurations
│   ├── security_groups/
│   │   └── main.tf              # Security group configurations
│   └── route53/
│       └── main.tf              # Route 53 DNS configurations
├── scripts/
│   └── userdata.sh              # User data script to configure Nginx
├── main.tf                      # Main Terraform configuration
├── variables.tf                 # Input variables for Terraform configuration
├── outputs.tf                   # Output configurations for Terraform
└── README.md                    # Documentation for the project

Setup Instructions:

1. Clone the Repository

Clone the repository to your local machine or directly to your AWS EC2 instance.

	git clone <repository_url>
	cd terraform-website-infrastructure

2. Configure AWS Credentials

Ensure your AWS credentials are configured properly. You can do this using the AWS CLI tool:

	aws configure

Alternatively, you can set your credentials by using environment variables (AWS Access Key, Secret Key, and Region).

3. Modify Variables

Edit the variables.tf file to specify your SSH key name and your IP address for SSH access.

variable "key_name" {
 description = "The name of the SSH key pair"
 type        = string
}

variable "ssh_ip" {
  description = "Your IP address for SSH access"
  type        = string
}
For example:

variable "key_name" {
  default = "my-ssh-key"
}

variable "ssh_ip" {
  default = "203.0.113.0/32"
}

4. Initialize Terraform

Run the following command to initialize the Terraform working directory. This will download necessary provider plugins and set up the configuration files:

		terraform init

5. Validate Configuration

Validate the Terraform configuration to ensure there are no errors:

		terraform validate

6. Plan the Deployment

Generate an execution plan that outlines the infrastructure changes Terraform will make:

		terraform plan

Review the plan to ensure everything looks correct.

7. Apply the Configuration

Apply the configuration to provision the infrastructure:

		terraform apply

Terraform will prompt for confirmation before applying the changes. Type yes to proceed with the deployment.

8. Access the Website

After Terraform successfully applies the configuration, your website should be accessible via the EC2 instance's public IP address. Open a browser and visit:

		http://<nginx_server_ip>

You should see the homepage of your website.

9. Clean Up
When you no longer need the infrastructure, you can destroy the resources created by Terraform using the following command:

		terraform destroy

This will terminate the EC2 instance, delete the VPC, and remove all other resources.

Security Considerations:

SSH Access: The EC2 instance is configured to only allow SSH access from the IP address specified in the ssh_ip variable in variables.tf. Ensure this is correctly set to limit access.
Nginx Configuration: The website is publicly accessible over HTTP. If needed, you can modify the Nginx configuration to support HTTPS using SSL certificates.

Future Enhancements (Optional):

Auto Scaling and Load Balancing: Implement an Auto Scaling Group and Load Balancer to improve availability and scalability.
RDS for Dynamic Content: Configure an Amazon RDS instance for dynamic content storage and integrate it with the website.
S3 for Static Files: Use Amazon S3 for storing and serving static files (such as images, CSS, JS) to improve performance and scalability.

License:

This project is licensed under the MIT License. See the LICENSE file for more details.
>>>>>>> d2eafeb (commit_midterm-terraform-project)
