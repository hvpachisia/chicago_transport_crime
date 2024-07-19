#script to teardown s3 servicees when no longer required
import boto3

s3_client = boto3.client('s3')
s3 = boto3.resource('s3')

def cleanup(bucket_name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    for item in bucket.objects.all():
        item.delete()
        
def delete_s3_resources(bucket_name):
    # Delete S3 bucket and its contents
    try:
        bucket = s3.Bucket(bucket_name)
        bucket.objects.all().delete()
        bucket.delete()
        print("S3 Bucket Deleted")
    except s3_client.exceptions.NoSuchBucket:
        print("S3 Bucket Already Deleted")

def main():
    cleanup('hvpachisia-chicago-crime')
    delete_s3_resources('hvpachisia-chicago-crime')

if __name__ == '__main__':
    main()
