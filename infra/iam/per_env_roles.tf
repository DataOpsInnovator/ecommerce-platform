terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
}

provider "aws" { region = var.aws_region }

# OIDC provider
resource "aws_iam_openid_connect_provider" "github" {
  url = "https://token.actions.githubusercontent.com"
  client_id_list   = ["sts.amazonaws.com"]
  thumbprint_list  = ["6938fd4d98bab03faadb97b34396831e3780aea1"]
}

# ---------- Policies ----------
# Prod
data "aws_iam_policy_document" "prod_doc" {
  statement {
    effect = "Allow"
    actions = ["s3:*"]
    resources = [
      "arn:aws:s3:::shopsmartlytoday-www-site",
      "arn:aws:s3:::shopsmartlytoday-www-site/*"
    ]
  }
  statement {
    effect = "Allow"
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
    effect = "Allow"
    actions = [
      "acm:RequestCertificate",
      "acm:DescribeCertificate",
      "acm:ListCertificates",
      "acm:DeleteCertificate"
    ]
    resources = ["*"]
  }
  statement {
    effect = "Allow"
    actions = [
      "route53:ChangeResourceRecordSets",
      "route53:GetChange",
      "route53:ListHostedZones",
      "route53:ListResourceRecordSets"
    ]
    resources = ["*"]
  }
}

resource "aws_iam_policy" "prod" {
  name   = "shopsmartlytoday-github-prod"
  policy = data.aws_iam_policy_document.prod_doc.json
}

# Staging
data "aws_iam_policy_document" "staging_doc" {
  statement {
    effect = "Allow"
    actions = ["s3:*"]
    resources = [
      "arn:aws:s3:::shopsmartlytoday-staging-site",
      "arn:aws:s3:::shopsmartlytoday-staging-site/*"
    ]
  }
  statement {
    effect = "Allow"
    actions = [
      "cloudfront:CreateInvalidation",
      "cloudfront:GetDistribution",
      "cloudfront:GetDistributionConfig",
      "cloudfront:ListDistributions",
      "cloudfront:UpdateDistribution"
    ]
    resources = ["*"]
  }
}

resource "aws_iam_policy" "staging" {
  name   = "shopsmartlytoday-github-staging"
  policy = data.aws_iam_policy_document.staging_doc.json
}

# Preview (write to preview buckets only; deny prod/staging explicitly)
data "aws_iam_policy_document" "preview_doc" {
  statement {
    effect = "Allow"
    actions = ["s3:*"]
    resources = [
      "arn:aws:s3:::shopsmartlytoday-*-site",
      "arn:aws:s3:::shopsmartlytoday-*-site/*"
    ]
  }
  statement {
    effect = "Deny"
    actions = ["s3:*"]
    resources = [
      "arn:aws:s3:::shopsmartlytoday-www-site",
      "arn:aws:s3:::shopsmartlytoday-www-site/*",
      "arn:aws:s3:::shopsmartlytoday-staging-site",
      "arn:aws:s3:::shopsmartlytoday-staging-site/*"
    ]
  }
  statement {
    effect = "Allow"
    actions = [
      "cloudfront:CreateInvalidation",
      "cloudfront:GetDistribution",
      "cloudfront:GetDistributionConfig",
      "cloudfront:ListDistributions"
    ]
    resources = ["*"]
  }
}

resource "aws_iam_policy" "preview" {
  name   = "shopsmartlytoday-github-preview"
  policy = data.aws_iam_policy_document.preview_doc.json
}

# ---------- Trust policies (replace YOUR-ORG if needed) ----------
data "aws_iam_policy_document" "trust_prod" {
  statement {
    effect = "Allow"
    principals { type = "Federated", identifiers = [aws_iam_openid_connect_provider.github.arn] }
    actions = ["sts:AssumeRoleWithWebIdentity"]
    condition {
      test = "StringLike"
      variable = "token.actions.githubusercontent.com:sub"
      values = ["repo:DataOpsInnovator/shopsmartlytoday-platform:ref:refs/heads/main"]
    }
    condition {
      test = "StringEquals"
      variable = "token.actions.githubusercontent.com:aud"
      values = ["sts.amazonaws.com"]
    }
  }
}

data "aws_iam_policy_document" "trust_staging" {
  statement {
    effect = "Allow"
    principals { type = "Federated", identifiers = [aws_iam_openid_connect_provider.github.arn] }
    actions = ["sts:AssumeRoleWithWebIdentity"]
    condition {
      test = "StringLike"
      variable = "token.actions.githubusercontent.com:sub"
      values = ["repo:DataOpsInnovator/shopsmartlytoday-platform:ref:refs/heads/dev"]
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
      values = ["repo:DataOpsInnovator/shopsmartlytoday-platform:ref:refs/heads/*"]
    }
    condition {
      test = "StringEquals"
      variable = "token.actions.githubusercontent.com:aud"
      values = ["sts.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "deploy_prod" {
  name               = "shopsmartlytoday-github-deploy-prod"
  assume_role_policy = data.aws_iam_policy_document.trust_prod.json
  max_session_duration = 3600
}
resource "aws_iam_role_policy_attachment" "attach_prod" {
  role       = aws_iam_role.deploy_prod.name
  policy_arn = aws_iam_policy.prod.arn
}

resource "aws_iam_role" "deploy_staging" {
  name               = "shopsmartlytoday-github-deploy-staging"
  assume_role_policy = data.aws_iam_policy_document.trust_staging.json
  max_session_duration = 3600
}
resource "aws_iam_role_policy_attachment" "attach_staging" {
  role       = aws_iam_role.deploy_staging.name
  policy_arn = aws_iam_policy.staging.arn
}

resource "aws_iam_role" "deploy_preview" {
  name               = "shopsmartlytoday-github-deploy-preview"
  assume_role_policy = data.aws_iam_policy_document.trust_preview.json
  max_session_duration = 3600
}
resource "aws_iam_role_policy_attachment" "attach_preview" {
  role       = aws_iam_role.deploy_preview.name
  policy_arn = aws_iam_policy.preview.arn
}

output "role_prod_arn"    { value = aws_iam_role.deploy_prod.arn }
output "role_staging_arn" { value = aws_iam_role.deploy_staging.arn }
output "role_preview_arn" { value = aws_iam_role.deploy_preview.arn }

variable "aws_region" { default = "us-east-1" }
