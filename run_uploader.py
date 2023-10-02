from uploader.uploader import Uploader
from config import s3_bucket_name, aws_access_key_id, aws_secret_access_key, gcs_project_id, gcs_bucket_name, gcs_credentials_file_path, s3_allowed_extensions, gcs_allowed_extensions

# Create an instance of the Uploader class
uploader = Uploader(
    s3_bucket_name,
    aws_access_key_id,
    aws_secret_access_key,
    gcs_project_id,
    gcs_bucket_name,
    gcs_credentials_file_path,
    s3_allowed_extensions,
    gcs_allowed_extensions
)

# Specify the root directory containing the files to upload
root_dir_name = "root_dir_name"  # Replace with your root_dir_name from where files needs to be uploaded "E:/old mempry backups/files"

# Upload files to both S3 and GCS
uploader.auto_upload(root_dir_name)
print("upload complete")
