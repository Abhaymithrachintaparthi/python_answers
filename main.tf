provider "aws" {
    region = "us-east-1"
    access_key = "AKIAZJNUPWVQCKGU6ALZ"
    secret_key = "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"
}
resource "aws_instance" "ubuntu" {
    ami = "ami-00874d747dde814fa"
    instance_type = "t2.micro"
    tags = {
      Name = "ubuntu"
    }
}
