import os
import traceback
from google.cloud import storage

class GCSUploader:
    """
    A class for uploading files to Google Cloud Storage (GCS).

    Attributes:
        gcs_project_id (str): The GCS project ID.
        gcs_bucket_name (str): The name of the GCS bucket to upload files to.
        gcs_credentials_file_path (str): The path to the GCS credentials JSON file.
        client (google.cloud.storage.Client): The GCS client used for communication.
        bucket_name (str): The name of the GCS bucket.
    """

    def __init__(self, gcs_project_id, gcs_bucket_name, gcs_credentials_file_path):
        """
        Initializes a GCSUploader instance.

        Args:
            gcs_project_id (str): The GCS project ID.
            gcs_bucket_name (str): The name of the GCS bucket to upload files to.
            gcs_credentials_file_path (str): The path to the GCS credentials JSON file.
        """
        # Set the environment variable for GCS credentials
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = gcs_credentials_file_path

        # Initialize the GCS client and bucket name
        self.client = storage.Client(project=gcs_project_id)
        self.bucket_name = gcs_bucket_name

    def upload_to_gcs(self, file_path_map):
        """
        Uploads files to Google Cloud Storage.

        Args:
            file_path_map (dict): A dictionary containing file paths to be uploaded.
                The keys are root directories, and the values are lists of tuples
                containing local file paths and GCS object names.
        """
        # Get the GCS bucket
        bucket = self.client.bucket(self.bucket_name)

        # Iterate over root directories and their associated files
        for root, path_list in file_path_map.items():
            if path_list:
                for item in path_list:
                    local_path = item[0]           # Local file path
                    gcs_object_name = item[1]      # GCS object name

                    try:
                        # Create a blob and upload the file to GCS
                        blob = bucket.blob(gcs_object_name)
                        blob.upload_from_filename(local_path)

                    except Exception as e:
                        # Handle upload errors and print detailed information
                        print("Error uploading ", local_path, " to ", gcs_object_name, ": ", str(e))
                        traceback.print_exc()
