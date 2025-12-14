
# The outputs.tf file in the vpc module should include any values that might be needed by other modules or resources outside the vpc module. 
# Commonly, this includes the VPC ID, subnet IDs, route table IDs, and internet gateway ID.

output "vpc_id" {
  description = "The ID of the VPC"
  value       = aws_vpc.my_vpc.id
}

output "public_subnet_id" {
  description = "The ID of the public subnet"
  value       = aws_subnet.public_subnet.id
}

output "private_subnet_id" {
  description = "The ID of the private subnet"
  value       = aws_subnet.private_subnet.id
}

output "internet_gateway_id" {
  description = "The ID of the internet gateway"
  value       = aws_internet_gateway.ig.id
}

output "public_route_table_id" {
  description = "The ID of the public route table"
  value       = aws_route_table.public_rt.id
}



# Explanation of Outputs:

# vpc_id: Provides the VPC ID, which is essential for other resources or modules that need to associate with this VPC.

# public_subnet_id and private_subnet_id: Output the subnet IDs for both the public and private subnets. These IDs are useful for deploying resources like EC2 instances or RDS databases in specific subnets.

# internet_gateway_id: Outputs the ID of the internet gateway, often necessary for resources needing internet access through this gateway.

# public_route_table_id: Provides the route table ID for the public subnet, which can be referenced if other resources need to associate with or modify routes in this table.