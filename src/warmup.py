import boto3
BUCKET_NAME = 'warmupbucket-iafm210525' # You can change this
TEXT_1 = 'text1.txt'
TEXT_2 = 'text2.txt'


def warm_up():
    s3client = boto3.client('s3')
    
    try:
        """Creates an S3 bucket."""
        # s3client.create_bucket(Bucket=BUCKET_NAME, CreateBucketConfiguration = {"LocationConstraint": 'eu-west-2'})
        # print(f"Bucket {BUCKET_NAME} Created")
        
        """Loads two text files to the bucket."""
        s3client.upload_file("data/text1.txt", BUCKET_NAME, TEXT_1)
        print(f"File uploaded to {BUCKET_NAME}")
        s3client.upload_file("data/text2.txt", BUCKET_NAME, TEXT_2)
        print(f"File uploaded to {BUCKET_NAME}")
        
        """Prints a listing of the files, saving the filenames in a readable list."""
        contents = s3client.list_objects_v2(Bucket=BUCKET_NAME)['Contents']
        contents_list = []
        for file in contents:
            contents_list.append(file['Key'])
        with open(f"{BUCKET_NAME}-contents.txt", "w") as file:
            file.write(f"{BUCKET_NAME} contents: {str(contents_list)}")
            print(f"contents written to file")
        
        """Reads one of the files and prints it to the console."""    
        text_file = s3client.get_object(Bucket=BUCKET_NAME, Key=TEXT_1)
        print(text_file['Body'].read().decode('utf-8') )
        
        """Delete objects from bucket"""
        for item in contents_list:
            s3client.delete_objects(Bucket=BUCKET_NAME, Delete={'Objects':[{'Key': item}]})
        print("objects deleted")
    except Exception:
        print("fail")
        

warm_up()

