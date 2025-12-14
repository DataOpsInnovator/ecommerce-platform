
# Output the Security Group ID:

output "nginx_sg_id" {
  description = "The ID of the security group"
  value = [aws_security_group.nginx_sg.id]  # Adjust this based on your resource name
}



