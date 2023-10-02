import os
import traceback
from uploader.s3uploader import S3Uploader
from uploader.gcsuploader import GCSUploader

class Uploader(S3Uploader, GCSUploader):
    def __init__(self, s3_bucket_name, aws_access_key_id, aws_secret_access_key, gcs_project_id, gcs_bucket_name, gcs_credentials_file_path, s3_allowed_extensions=None, gcs_allowed_extensions=None, **kwargs):
        # Initialize allowed extensions for both S3 and GCS
        self.s3_allowed_extensions = s3_allowed_extensions or [".jpg", ".png", ".svg", ".webp", ".mp3", ".mp4", ".mpeg4", ".wmv", ".3gp", ".webm"]
        self.gcs_allowed_extensions = gcs_allowed_extensions or [".doc", ".docx", ".csv", ".pdf"]
        
        # Call the constructors for both S3Uploader and GCSUploader
        self.s3_uploader = S3Uploader(s3_bucket_name, aws_access_key_id, aws_secret_access_key, **kwargs)
        self.gcs_uploader = GCSUploader(gcs_project_id, gcs_bucket_name, gcs_credentials_file_path, **kwargs)

    def file_dir_map(self, root_dir_name):
        s3_file_dict = {}
        gcs_file_dict = {}
        for root, _, files in os.walk(root_dir_name):
            s3_files = []
            gcs_files = []
            for file in files:
                file_path = os.path.join(root, file)
                include_in_s3 = self.has_extension(file, self.s3_allowed_extensions)
                include_in_gcs = self.has_extension(file, self.gcs_allowed_extensions)

                if include_in_s3 or include_in_gcs:
                    relative_path = os.path.relpath(file_path, root_dir_name)
                    file_key = os.path.join(relative_path.replace(os.path.sep, '/'))

                if include_in_s3:
                    s3_files.append((file_path, file_key))

                if include_in_gcs:
                    gcs_files.append((file_path, file_key))

            s3_file_dict[root] = s3_files
            gcs_file_dict[root] = gcs_files
        file_dir_dict = {"s3_files": s3_file_dict, "gcs_files": gcs_file_dict}
        return {"s3_files": s3_file_dict, "gcs_files": gcs_file_dict}

    def has_extension(self, file_path, allowed_extensions):
        file_extension = os.path.splitext(file_path)[1].lower()
        return file_extension in allowed_extensions

    def auto_upload(self, root_dir_name):
        file_path_map = self.file_dir_map(root_dir_name)
        self.s3_uploader.upload_to_s3(file_path_map["s3_files"])
        self.gcs_uploader.upload_to_gcs(file_path_map["gcs_files"])
        return None  # Return None for success, raise an exception for errors

