terraform {
  backend "s3" {
    bucket         = "shopsmartlytoday-tfstate"
    key            = "env/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "shopsmartlytoday-terraform-lock"
    encrypt        = true
  }
}
