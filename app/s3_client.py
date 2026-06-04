import boto3

BUCKET_NAME = "taskhub-bucket"

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

def upload_file(filename, data):
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=filename,
        Body=data
    )
    return f"s3://{BUCKET_NAME}/{filename}"


def list_files():
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    return response.get("Contents", [])


def download_file(filename):
    return s3.get_object(Bucket=BUCKET_NAME, Key=filename)["Body"].read()