#!/bin/bash

# Replace with your GitHub username and repository name
GITHUB_USER="Frz-Ehr"
REPO_NAME="raspwidget"

# Directory where the repository should be cloned
DIR="$HOME/${REPO_NAME}"

# Check if the directory already exists
if [ -d "$DIR" ]; then
  # If the directory exists, navigate to it and pull the latest changes
  cd "$DIR" || exit
  git fetch
  git reset --hard origin/main
else
  # If the directory does not exist, clone the repository
  git clone "https://github.com/${GITHUB_USER}/${REPO_NAME}.git" "$DIR"
fi

exit
