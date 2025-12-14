# In terraform/main.tf, set up the provider and call your modules.
# This main.tf file calls each module (VPC, security group, and EC2 instance).

provider "aws" {
  region = "us-east-1"
}

# VPC Module block:
# Passing Values When Calling the Module
# When calling the vpc module from the root module, pass any desired values for these variables, or rely on defaults:

module "vpc" {
  source              = "./modules/vpc"
  vpc_cidr            = "10.0.0.0/16"
  public_subnet_cidr  = "10.0.1.0/24"
  private_subnet_cidr = "10.0.2.0/24"
  availability_zone_public  = "us-east-1a"
  availability_zone_private = "us-east-1b"
}

# Security Groups Module block:

module "security_groups" {
  source = "./modules/security_groups"
  #vpc_id = var.vpc_id
  vpc_id = module.vpc.vpc_id            # Pass VPC ID from the vpc module
  ssh_ip = var.ssh_ip                   # Pass the SSH IP from root variables
}

# EC2 Module block:

module "ec2" {
  source           = "./modules/ec2"
  vpc_id           = module.vpc.vpc_id
  public_subnet_id = module.vpc.public_subnet_id            # Passing public_subnet_id from the vpc module
  security_groups  = module.security_groups.nginx_sg_id
  key_name         = var.key_name

  # ami              = var.ami_id      
  # instance_type    = "t2.micro" 
  # user_data        = file("scripts/userdata.sh")
}

# This setup makes ami and instance_type configurable from the root module while allowing the ec2 module 
# to reference them within the aws_instance resource.

