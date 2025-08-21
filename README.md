# shopsmartlytoday-platform (Monorepo)
Monorepo for frontend, backend (future), and AWS infrastructure.

## Structure
- `frontend/` – static site (your HTML/CSS)
- `backend/` – placeholder for future APIs
- `infra/` – Terraform (prod, staging, root redirect, previews via module)
- `.github/workflows/` – CI/CD pipelines (prod, staging, preview branches)
- `docs/` – architecture diagram

## Quick Start
```bash
cd infra/environments
terraform init
terraform apply -var='aws_region=us-east-1' -var='project_name=shopsmartlytoday' -var='domain_name=shopsmartlytoday.com'
```


---

## Remote State (S3 + DynamoDB)
Bootstrap once:
```bash
cd infra/state-bootstrap
terraform init
terraform apply -var='aws_region=us-east-1' -var='state_bucket=shopsmartlytoday-tfstate' -var='lock_table=shopsmartlytoday-terraform-lock'
```

Then use remote backend for environments:
```bash
cd ../environments
terraform init   # will detect and use the S3 backend
terraform workspace new prod || true
terraform workspace select prod
terraform apply -var='aws_region=us-east-1' -var='project_name=shopsmartlytoday' -var='domain_name=shopsmartlytoday.com'

terraform workspace new staging || true
terraform workspace select staging
terraform apply -var='aws_region=us-east-1' -var='project_name=shopsmartlytoday' -var='domain_name=shopsmartlytoday.com'
```

## GitHub OIDC + Roles (Per-Env)
- `infra/iam/github-oidc.tf` creates:
  - OIDC provider
  - `shopsmartlytoday-deploy-prod-role` (main)
  - `shopsmartlytoday-deploy-staging-role` (dev)
  - `shopsmartlytoday-preview-readonly-role` (all other branches)
- Update `YOUR-ORG` and `YOUR_AWS_ACCOUNT_ID` before applying.
- After applying, the GitHub Actions workflow uses `role-to-assume` per environment.


---

## 🏗 Terraform Remote State (S3 + DynamoDB)

Bootstrap once:
```bash
cd infra/state-backend
terraform init
terraform apply -var='aws_region=us-east-1' -var='project_name=shopsmartlytoday'
```

This creates:
- S3 bucket: `shopsmartlytoday-tfstate`
- DynamoDB lock table: `shopsmartlytoday-tflock`

## 🔐 GitHub OIDC + Per-Env Roles

Deploy IAM/OIDC and roles (replace YOUR-ORG in HCL first):
```bash
cd infra/iam
terraform init
terraform apply -var='aws_region=us-east-1'
```

Copy the output ARNs into `.github/workflows/deploy.yml`:
- `shopsmartlytoday-github-deploy-prod`
- `shopsmartlytoday-github-deploy-staging`
- `shopsmartlytoday-github-deploy-preview`

## 🚀 Environments (use remote state)

**Prod**:
```bash
cd infra/environments
terraform init -reconfigure
terraform workspace select prod || terraform workspace new prod
terraform apply -var='aws_region=us-east-1' -var='project_name=shopsmartlytoday' -var='domain_name=shopsmartlytoday.com'
```

**Staging**:
```bash
cd infra/environments
terraform init -reconfigure
terraform workspace select staging || terraform workspace new staging
terraform apply -var='aws_region=us-east-1' -var='project_name=shopsmartlytoday' -var='domain_name=shopsmartlytoday.com'
```


---

## 🌐 Enterprise Workspaces (prod, staging, preview-branches)

We use **Terraform workspaces** with a single backend key pattern:
`envs/${terraform.workspace}/terraform.tfstate`

### Initialize & create workspaces
```bash
cd infra/environments
terraform init -reconfigure

# create/select workspaces
terraform workspace new prod || true
terraform workspace new staging || true

terraform workspace select prod
terraform apply -var='aws_region=us-east-1' -var='project_name=shopsmartlytoday' -var='domain_name=shopsmartlytoday.com'

terraform workspace select staging
terraform apply -var='aws_region=us-east-1' -var='project_name=shopsmartlytoday' -var='domain_name=shopsmartlytoday.com'
```
