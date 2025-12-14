# Define Outputs in outputs.tf
# Create an outputs.tf file to retrieve useful outputs from the deployment.
# Outputs to capture the public IP of EC2 instance

output "nginx_server_ip" {
  value = module.ec2.nginx_public_ip
}

output "vpc_id" {
  value = module.vpc.vpc_id
}

output "nginx_sg_id" {
  value = module.security_groups.nginx_sg_id
}

# output "nginx_sg_id" {
#   value = aws_security_group.nginx_sg_id 
# }