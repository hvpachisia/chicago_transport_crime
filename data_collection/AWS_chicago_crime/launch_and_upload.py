#script to launch and create S3 buckets and upload required data
import boto3

def create_s3_bucket():
    s3 = boto3.resource('s3')
    # Create a new bucket to store your files
    BUCKETNAME = 'hvpachisia-chicago-crime'
    s3.create_bucket(Bucket=BUCKETNAME)
    bucket = s3.Bucket( BUCKETNAME )
    return bucket

def upload_data_to_s3():
    s3_client = boto3.client('s3')
    local_folder= '/Users/Harsh/Desktop/01_Projects/computing/data/'
    bucket_name = 'hvpachisia-chicago-crime'
    list_of_file_paths = [
        'crimes.csv',
        'COVID-19_Daily_Cases__Deaths__and_Hospitalizations_20240522.csv',
        'Public_Health_Statistics_-_Selected_public_health_indicators_by_Chicago_community_area_-_Historical_20240522.csv',
        'communities.csv'
                          ]
    for file in list_of_file_paths:
        s3_file_path = 'raw_data/' + file
        s3_client.upload_file(local_folder + file, bucket_name, s3_file_path)
    return print("Upload of all datasets complete.")


def main():
    bucket = create_s3_bucket()
    print("Bucket", bucket, "created")
    upload_data_to_s3()

if __name__ == '__main__':
    main()
