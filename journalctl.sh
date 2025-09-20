#!/bin/bash
set -e
LOG_FILE="journalctl.log"
sudo journalctl > "$LOG_FILE"

# Replace with your actual bucket name
S3_BUCKET="s3://s3-bucket-name"

aws s3 cp "$LOG_FILE" "$S3_BUCKET"
