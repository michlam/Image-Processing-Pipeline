#!/bin/bash

S3_FILE_PATH=$1

# exit if argument is not provided
if [ -z "$S3_FILE_PATH" ]; then
  echo "Usage: init.sh <s3_file_path>"
  exit 1
fi

# copy file from s3 bucket to container
aws s3 cp "s3://openalpr/$S3_FILE_PATH" "/data/$S3_FILE_PATH"

# run openalpr
exec alpr "/data/$S3_FILE_PATH"