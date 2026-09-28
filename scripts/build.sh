#!/usr/bin/env bash
set -euo pipefail

mkdir -p dist

cat > dist/release.txt <<EOF
commit=${GITHUB_SHA}
workflow=${GITHUB_WORKFLOW}
run_id=${GITHUB_RUN_ID}
EOF

echo "Build created:"
cat dist/release.txt