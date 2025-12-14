# modules/vpc/variables.tf
# Define these variables in the variables.tf file within the vpc module:

# In the vpc module, several variables can be parameterized to make the code reusable and adaptable to different configurations. 

variable "vpc_id" {
  description = "The VPC ID where the instance will be deployed"
  type        = string
  default     = "vpc-02543443241f7e9ba"
}

variable "vpc_cidr" {
  description = "The CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"  # Set a default or override when calling the module. This will be used as the default value unless it is overridden. When you call the module, you can pass a different value for this variable, and that new value will take precedence over the default.
}

variable "public_subnet_cidr" {
  description = "The CIDR block for the public subnet"
  type        = string
  default     = "10.0.1.0/24"
}

variable "private_subnet_cidr" {
  description = "The CIDR block for the private subnet"
  type        = string
  default     = "10.0.2.0/24"
}

variable "availability_zone_public" {
  description = "Availability zone for the public subnet"
  type        = string
  default     = "us-east-1a"
}

variable "availability_zone_private" {
  description = "Availability zone for the private subnet"
  type        = string
  default     = "us-east-1b"
}


# variable "public_subnet_id" {
#   description = "The public subnet ID for the EC2 instance"
#   type        = string
#   default = "public-subnet"
# }