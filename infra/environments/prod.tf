terraform {
  backend "s3" {
    bucket         = "shopsmartlytoday-tfstate"
    key            = "envs/${terraform.workspace}/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "shopsmartlytoday-tflock"
    encrypt        = true
  }
}

terraform {
  required_version = ">= 1.6.0"
  required_providers { aws = { source = "hashicorp/aws", version = ">= 5.0" } }
}
provider "aws" { region = var.aws_region }

module "prod" {
  source       = "../modules/env"
  aws_region   = var.aws_region
  project_name = var.project_name
  domain_name  = var.domain_name
  subdomain    = "www"
}

# Apex redirect distribution
resource "aws_cloudfront_function" "root_redirect" {
  name    = "${var.project_name}-root-redirect"
  runtime = "cloudfront-js-1.0"
  publish = true
  code    = <<EOF
function handler(event) {
  var request = event.request;
  return {
    statusCode: 301,
    statusDescription: "Moved Permanently",
    headers: { "location": { "value": "https://www.${var.domain_name}" } }
  };
}
EOF
}

resource "aws_s3_bucket" "root" { bucket = "${var.project_name}-root-redirect" }

resource "aws_cloudfront_distribution" "root" {
  enabled = true
  origins {
    origin_id   = "s3-${aws_s3_bucket.root.bucket}"
    domain_name = aws_s3_bucket.root.bucket_regional_domain_name
  }
  default_cache_behavior {
    target_origin_id       = "s3-${aws_s3_bucket.root.bucket}"
    viewer_protocol_policy = "redirect-to-https"
    allowed_methods        = ["GET", "HEAD"]
    cached_methods         = ["GET", "HEAD"]
    function_associations {
      event_type   = "viewer-request"
      function_arn = aws_cloudfront_function.root_redirect.arn
    }
  }
  viewer_certificate { cloudfront_default_certificate = true }
  aliases = ["${var.domain_name}"]
}

data "aws_route53_zone" "primary" { name = var.domain_name, private_zone = false }

resource "aws_route53_record" "apex" {
  zone_id = data.aws_route53_zone.primary.zone_id
  name    = var.domain_name
  type    = "A"
  alias {
    name                   = aws_cloudfront_distribution.root.domain_name
    zone_id                = aws_cloudfront_distribution.root.hosted_zone_id
    evaluate_target_health = false
  }
}
