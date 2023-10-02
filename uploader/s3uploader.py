import boto3

class S3Uploader:
    """
    A class for uploading files to Amazon S3.

    Attributes:
        s3_bucket_name (str): The name of the S3 bucket to upload files to.
        aws_access_key_id (str): The AWS access key ID.
        aws_secret_access_key (str): The AWS secret access key.
        s3_client (boto3.client): The S3 client used for communication.
    """

    def __init__(self, s3_bucket_name, aws_access_key_id, aws_secret_access_key):
        """
        Initializes an S3Uploader instance.

        Args:
            s3_bucket_name (str): The name of the S3 bucket to upload files to.
            aws_access_key_id (str): The AWS access key ID.
            aws_secret_access_key (str): The AWS secret access key.
        """
        # Initialize attributes
        self.bucket_name = s3_bucket_name
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key

        # Create an S3 client instance
        self.s3_client = boto3.client('s3', aws_access_key_id=self.aws_access_key_id, aws_secret_access_key=self.aws_secret_access_key)

    def upload_to_s3(self, file_path_map):
        """
        Uploads files to Amazon S3.

        Args:
            file_path_map (dict): A dictionary containing file paths to be uploaded.
                The keys are root directories, and the values are lists of tuples
                containing local file paths and S3 object keys.
        """
        # Iterate over root directories and their associated files
        for root, path_list in file_path_map.items():
            if path_list:
                for item in path_list:
                    local_path = item[0]    # Local file path
                    s3_key = item[1]        # S3 object key

                    try:
                        # Upload the file to the S3 bucket
                        self.s3_client.upload_file(local_path, self.bucket_name, s3_key)

                    except Exception as e:
                        # Handle upload errors and print detailed information
                        print("Error uploading '{0}' to '{1}': {2}".format(local_path, s3_key, str(e)))
                        raise  # Re-raise the original exception for better debugging
