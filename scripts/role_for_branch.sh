
#!/usr/bin/env bash
set -euo pipefail
BRANCH="${1:-}"
ACCOUNT_ID="${AWS_ACCOUNT_ID:-}"
if [[ -z "$BRANCH" || -z "$ACCOUNT_ID" ]]; then
  echo "Usage: AWS_ACCOUNT_ID=123456789012 role_for_branch.sh <branch>" >&2
  exit 1
fi

ROLE="shopsmartlytoday-github-deploy-preview"
if [[ "$BRANCH" == "main" ]]; then
  ROLE="shopsmartlytoday-github-deploy-prod"
elif [[ "$BRANCH" == "dev" ]]; then
  ROLE="shopsmartlytoday-github-deploy-staging"
fi

echo "arn:aws:iam::${ACCOUNT_ID}:role/${ROLE}"
