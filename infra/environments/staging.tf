terraform {
  backend "s3" {
    bucket         = "shopsmartlytoday-tfstate"
    key            = "envs/${terraform.workspace}/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "shopsmartlytoday-tflock"
    encrypt        = true
  }
}

provider "aws" { region = var.aws_region }
module "staging" {
  source       = "../modules/env"
  aws_region   = var.aws_region
  project_name = var.project_name
  domain_name  = var.domain_name
  subdomain    = "staging"
}
