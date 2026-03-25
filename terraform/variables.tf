variable "aws_region"       { default = "us-east-1" }
variable "instance_type"    { default = "t3.medium" }
variable "ami_id"           { default = "ami-0c02fb55956c7d316" } # Amazon Linux 2 us-east-1
variable "public_key_path"  { default = "~/.ssh/id_rsa.pub" }