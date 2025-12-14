
output "nginx_public_ip" {
  description = "The public IP of the NGINX instance"
  value       = aws_instance.nginx_server.public_ip
}
