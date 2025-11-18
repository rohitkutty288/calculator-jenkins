#AWS provider

provider "aws" {
   region = "us-east-1"
}

#Create the instance at aws

resource "aws_instance" "Terraform_tf" {
   ami = "ami-0157af9aea2eef346"
   instance_type = "t2.micro"

   tags = {
    name = "my-terraform"
  }
}

#Create s3 bucket for same ami

resource "aws_s3_bucket" "my_terraform_s3bucket" {
   bucket = "terraform-myrohit-s3"

   tags = {
   name = "my-terraform-s3"
  }
}

#Set ownership in s3

resource "aws_s3_bucket_ownership_controls" "s3_ownership" {
    bucket = aws_s3_bucket.my_terraform_s3bucket.id

    rule {
      object_ownership = "BucketOwnerEnforced"
  }
}
