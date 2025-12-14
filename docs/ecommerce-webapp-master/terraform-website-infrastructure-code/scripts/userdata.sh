#!/bin/bash

# Update the system
sudo yum update -y

# Install Nginx
sudo amazon-linux-extras enable nginx1
sudo yum install -y nginx

# Start Nginx service
sudo systemctl start nginx
sudo systemctl enable nginx

# Create the custom Nginx configuration file for the website
sudo bash -c 'cat <<EOL > /etc/nginx/conf.d/mywebsite.conf
server {
    listen 80;
    root /usr/share/nginx/html;               # Path to the default directory for Nginx
    index index.html;

    location / {
        try_files \$uri \$uri/ =404;           # Serve the file if it exists, or return 404
    }
}
EOL'

# Copy website files to the default Nginx directory
# Assuming the website files are in '/mywebsite' directory

# sudo cp -r /mywebsite/* /usr/share/nginx/html/

# Ensure the website files are now in '/home/ec2-user/mywebsite'

# sudo cp -r /home/ec2-user/mywebsite/* /usr/share/nginx/html/
  sudo cp -r /C:\Repositories\awsclass102024\terraform-website-infrastructure-2\mywebsite/* /usr/share/nginx/html/

# Set the correct permissions for the Nginx user to access the files
sudo chown -R nginx:nginx /usr/share/nginx/html/
sudo chmod -R 755 /usr/share/nginx/html/

# Restart Nginx to apply the new configuration
sudo systemctl restart nginx
