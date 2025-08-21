terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# OIDC provider for GitHub Actions
resource "aws_iam_openid_connect_provider" "github" {
  url = "https://token.actions.githubusercontent.com"
  client_id_list   = ["sts.amazonaws.com"]
  thumbprint_list  = ["6938fd4d98bab03faadb97b34396831e3780aea1"]
}

# Shared policy doc fragments
data "aws_iam_policy_document" "deploy_permissions_shared" {
  statement {
    sid     = "S3SiteBuckets"
    effect  = "Allow"
    actions = ["s3:*"]
    resources = [
      "arn:aws:s3:::shopsmartlytoday-*",
      "arn:aws:s3:::shopsmartlytoday-*/*"
    ]
  }

  statement {
    sid     = "CloudFrontInvalidate"
    effect  = "Allow"
    actions = [
      "cloudfront:CreateInvalidation",
      "cloudfront:GetDistribution",
      "cloudfront:GetDistributionConfig",
      "cloudfront:ListDistributions",
      "cloudfront:UpdateDistribution"
    ]
    resources = ["*"]
  }

  statement {
    sid     = "ACMCerts"
    effect  = "Allow"
    actions = [
      "acm:RequestCertificate",
      "acm:DescribeCertificate",
      "acm:ListCertificates",
      "acm:DeleteCertificate"
    ]
    resources = ["*"]
  }

  statement {
    sid     = "Route53Change"
    effect  = "Allow"
    actions = [
      "route53:ChangeResourceRecordSets",
      "route53:GetChange",
      "route53:ListHostedZones",
      "route53:ListResourceRecordSets"
    ]
    resources = ["*"]
  }
}

# Environment-scoped policies (you can tighten S3/CF further by naming exact buckets/IDs)
resource "aws_iam_policy" "deploy_prod" {
  name   = "shopsmartlytoday-github-deploy-prod"
  policy = data.aws_iam_policy_document.deploy_permissions_shared.json
}

resource "aws_iam_policy" "deploy_staging" {
  name   = "shopsmartlytoday-github-deploy-staging"
  policy = data.aws_iam_policy_document.deploy_permissions_shared.json
}

# Read-only preview role (no write)
data "aws_iam_policy_document" "preview_readonly" {
  statement {
    sid     = "ReadOnly"
    effect  = "Allow"
    actions = [
      "s3:ListAllMyBuckets",
      "s3:ListBucket",
      "s3:GetObject",
      "cloudfront:ListDistributions",
      "cloudfront:GetDistribution",
      "route53:ListHostedZones",
      "route53:ListResourceRecordSets",
      "acm:ListCertificates",
      "acm:DescribeCertificate"
    ]
    resources = ["*"]
  }
}

resource "aws_iam_policy" "preview_readonly" {
  name   = "shopsmartlytoday-github-preview-readonly"
  policy = data.aws_iam_policy_document.preview_readonly.json
}

# Trust policies - replace YOUR-ORG if needed
locals {
  repo_sub_main   = "repo:YOUR-ORG/shopsmartlytoday-platform:ref:refs/heads/main"
  repo_sub_dev    = "repo:YOUR-ORG/shopsmartlytoday-platform:ref:refs/heads/dev"
  repo_sub_pre    = "repo:YOUR-ORG/shopsmartlytoday-platform:ref:refs/heads/*"
}

data "aws_iam_policy_document" "trust_main" {
  statement {
    effect = "Allow"
    principals { type = "Federated", identifiers = [aws_iam_openid_connect_provider.github.arn] }
    actions = ["sts:AssumeRoleWithWebIdentity"]
    condition {
      test = "StringLike"
      variable = "token.actions.githubusercontent.com:sub"
      values = [local.repo_sub_main]
    }
    condition {
      test = "StringEquals"
      variable = "token.actions.githubusercontent.com:aud"
      values = ["sts.amazonaws.com"]
    }
  }
}

data "aws_iam_policy_document" "trust_dev" {
  statement {
    effect = "Allow"
    principals { type = "Federated", identifiers = [aws_iam_openid_connect_provider.github.arn] }
    actions = ["sts:AssumeRoleWithWebIdentity"]
    condition {
      test = "StringLike"
      variable = "token.actions.githubusercontent.com:sub"
      values = [local.repo_sub_dev]
    }
    condition {
      test = "StringEquals"
      variable = "token.actions.githubusercontent.com:aud"
      values = ["sts.amazonaws.com"]
    }
  }
}

data "aws_iam_policy_document" "trust_preview" {
  statement {
    effect = "Allow"
    principals { type = "Federated", identifiers = [aws_iam_openid_connect_provider.github.arn] }
    actions = ["sts:AssumeRoleWithWebIdentity"]
    condition {
      test = "StringLike"
      variable = "token.actions.githubusercontent.com:sub"
      values = [local.repo_sub_pre]
    }
    condition {
      test = "StringEquals"
      variable = "token.actions.githubusercontent.com:aud"
      values = ["sts.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "deploy_prod" {
  name               = "shopsmartlytoday-deploy-prod-role"
  assume_role_policy = data.aws_iam_policy_document.trust_main.json
  max_session_duration = 3600
}
resource "aws_iam_role_policy_attachment" "deploy_prod_attach" {
  role       = aws_iam_role.deploy_prod.name
  policy_arn = aws_iam_policy.deploy_prod.arn
}

resource "aws_iam_role" "deploy_staging" {
  name               = "shopsmartlytoday-deploy-staging-role"
  assume_role_policy = data.aws_iam_policy_document.trust_dev.json
  max_session_duration = 3600
}
resource "aws_iam_role_policy_attachment" "deploy_staging_attach" {
  role       = aws_iam_role.deploy_staging.name
  policy_arn = aws_iam_policy.deploy_staging.arn
}

resource "aws_iam_role" "preview_readonly" {
  name               = "shopsmartlytoday-preview-readonly-role"
  assume_role_policy = data.aws_iam_policy_document.trust_preview.json
  max_session_duration = 3600
}
resource "aws_iam_role_policy_attachment" "preview_readonly_attach" {
  role       = aws_iam_role.preview_readonly.name
  policy_arn = aws_iam_policy.preview_readonly.arn
}

variable "aws_region" { type = string, default = "us-east-1" }
