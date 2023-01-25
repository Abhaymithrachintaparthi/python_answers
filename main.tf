provider "aws" {
    region = "us-east-1"
    access_key = "AKIAZJNUPWVQJ3EJQA4Q"
    secret_key = "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"
}
resource "aws_instance" "ubuntu" {
    ami = "ami-00874d747dde814fa"
    instance_type = "t2.micro"
    subnet_id = "subnet-0df3ef6c4b95f87cd"
    security_groups = [ "sg-01f685398241499a7" ]
    tags = {
      "name" = "ec2_instance"
    }
}
