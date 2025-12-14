# Define Variables in variables.tf:

# Create a variables.tf file to define input variables.
# Create a variables.tf file to define variables for the SSH key and IP address.

variable "vpc_id" {
  description = "The VPC ID where the instance will be deployed"
  type        = string
  default     = "vpc-02543443241f7e9ba"
}
variable "public_subnet_id" {
  description = "The public subnet ID for the EC2 instance"
  type        = string
  default = "public-subnet"
}

variable "security_groups" {
  description = "Security group ID(s) for the EC2 instance"
  type        = list(string)
  default     = ["nginx_sg"]
}

variable "key_name" {
  description = "The SSH key pair name for EC2 access"
  type        = string
  default     = "my-ssh-key"
}

variable "ssh_ip" {
  description = "The CIDR block or IP address allowed to access via SSH"
  type        = string
  default     = "0.0.0.0/0"
}

variable "ami_id" {
   description = "AMI ID for the EC2 instance"
   type        = string
    default     = "ami-01e3c4a339a264cc9"
 }

# variable "user_data" {
#   description = "User data to configure the instance on startup"
#   type        = string
#   default     = null
# }
