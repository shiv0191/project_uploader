# S3 Configuration
s3_bucket_name = "your_s3_bucket_name"  # Replace with your S3 bucket name
aws_access_key_id = "your_aws_access_key_id"  # Replace with your AWS access key ID
aws_secret_access_key = "your_aws_secret_access_key"  # Replace with your AWS secret access key

# GCS Configuration
gcs_project_id = "your_gcs_project_id"  # Replace with your GCP project ID
gcs_bucket_name = "your_gcs_bucket_name"  # Replace with your GCS bucket name
gcs_credentials_file_path = "your_gcs_credentials_file_path"  # Replace with the path to your GCS credentials file

# Allowed Extensions for Upload
s3_allowed_extensions = [".jpg", ".png", ".svg", ".webp", ".mp3", ".mp4", ".mpeg4", ".wmv", ".3gp", ".webm"]  # Replace with S3 allowed extensions
gcs_allowed_extensions = [".doc", ".docx", ".csv", ".pdf"]  # Replace with GCS allowed extensions
