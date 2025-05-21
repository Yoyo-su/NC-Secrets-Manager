import boto3

def warm_up():
    s3client = boto3.client("s3")
    try:
        response = s3client.create_bucket(Bucket='warmup_bucket_IAFM_2105', CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'},)
        print(response)
    except:
        print("fail")

