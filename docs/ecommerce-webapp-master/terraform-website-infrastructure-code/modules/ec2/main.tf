# Create an EC2 instance with Nginx setup and 
# Set up the EC2 instance, referencing the security group and key_name passed from the root.
# Required provider

resource "aws_instance" "nginx_server" {
  ami           = var.ami_id
  instance_type = var.instance_type
  subnet_id     = var.public_subnet_id
  security_groups = var.security_groups
  associate_public_ip_address = true
  key_name      = var.key_name
  user_data = file("${path.module}/../../scripts/userdata.sh")  # Reference userdata.sh from the root directory

  tags = {
    Name = "nginx_server"
  }

}





