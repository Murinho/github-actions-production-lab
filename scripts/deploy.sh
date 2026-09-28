#!/usr/bin/env bash
set -euo pipefail

if [[ -z "${LAB_DEPLOY_TOKEN:-}" ]]; then
    echo "::error::LAB_DEPLOY_TOKEN is unavailable"
    exit 1
fi

if [[ ! -f dist/release.txt ]]; then
    echo "::error::dist/release.txt does not exist"
    exit 1
fi

echo "Starting simulated production deployment..."

cat dist/release.txt

sleep "${DEPLOY_SLEEP_SECONDS:-5}"

echo "Simulated production deployment completed."