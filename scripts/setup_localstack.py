import boto3
import os

endpoint = "http://localhost:4566"

s3 = boto3.client(
    "s3",
    endpoint_url=endpoint,
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

bucket = "taskhub-bucket"

try:
    s3.create_bucket(Bucket=bucket)
    print("Bucket created")
except Exception as e:
    print("Bucket exists or error:", e)