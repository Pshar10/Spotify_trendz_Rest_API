output "public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.flask_ec2.public_ip
}
