#!/usr/bin/env bash

set -eu

git config user.name "$GITHUB_ACTOR"
git config user.email "${GITHUB_ACTOR}@bots.github.com"

repo_uri="https://x-access-token:${ACCESS_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"



cd "$GITHUB_WORKSPACE"

date_str=$(date +%Y-%m-%d)
commit_tag=v$date_str
commit_msg="Deployed forecast ${date_str}"

git add forecast_plots
git commit -am "${commit_msg}"
git tag --force $commit_tag
git push $repo_uri master -f --tags

if [ $? -ne 0 ]; then
    echo "nothing to commit"
    exit 0
fi