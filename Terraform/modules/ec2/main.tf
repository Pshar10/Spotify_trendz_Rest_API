resource "aws_instance" "flask_ec2" {
  ami             = var.ami
  instance_type   = var.instance_type
  key_name        = var.key_name
  security_groups = [var.security_group_id]

  user_data = file("${path.module}/user_data.sh")

  tags = {
    Name = "FlaskApp-EC2"
  }
}
