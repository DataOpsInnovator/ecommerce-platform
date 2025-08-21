
.PHONY: init-state init-iam init-env prod staging

AWS_REGION ?= us-east-1

init-state:
	cd infra/state-backend && terraform init && terraform apply -auto-approve -var="aws_region=$(AWS_REGION)" -var="project_name=shopsmartlytoday"

init-iam:
	cd infra/iam && terraform init && terraform apply -auto-approve -var="aws_region=$(AWS_REGION)"

init-env:
	cd infra/environments && terraform init -reconfigure

prod:
	cd infra/environments && terraform workspace select prod || terraform workspace new prod && terraform apply -auto-approve -var="aws_region=$(AWS_REGION)" -var="project_name=shopsmartlytoday" -var="domain_name=shopsmartlytoday.com"

staging:
	cd infra/environments && terraform workspace select staging || terraform workspace new staging && terraform apply -auto-approve -var="aws_region=$(AWS_REGION)" -var="project_name=shopsmartlytoday" -var="domain_name=shopsmartlytoday.com"
