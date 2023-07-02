provider "aws" {
    region = "ap-south-1"
}

variable "name" {
  type = string
}

variable "nodecount" {
  type = number
}

resource "aws_instance" "hadoop" {
  count  = var.nodecount
  ami           = "ami-003b12a9a1ee83922"
  instance_type = "t3.micro"
  vpc_security_group_ids = ["sg-1e994361"]
  key_name = "hadoop"
  subnet_id = "subnet-07c5918859d627e1e"
  tags = {
    Name = var.nodecount > 1 ? "${var.name}-${count.index + 1}" : var.name 
  }
}

resource "local_file" "inventory" {
  content  = <<-EOT
[namenode]
${try(aws_instance.hadoop.0.public_ip, "")}

[datanode]
${try(aws_instance.hadoop.1.public_ip, "")}
${try(aws_instance.hadoop.2.public_ip, "")}
${try(aws_instance.hadoop.3.public_ip, "")}

[all:vars]
ansible_user=ec2-user
  EOT
  filename = "../playbooks/hadoop/inventory"
}