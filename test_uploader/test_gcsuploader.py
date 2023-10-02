import os
from unittest.mock import MagicMock, patch
import pytest
from google.cloud import storage
from uploader.gcsuploader import GCSUploader

# Define the configuration variable for credentials path
MOCK_CREDENTIALS_PATH = "google\cred.json"

# Define parameters for testing
project_id_1 = 'project_id_1'
bucket_name_1 = 'bucket_name_1'

test_params = [
    (project_id_1, bucket_name_1),
    # Add more test scenarios as needed
]

# Define file_path_map and expected_file_path
file_path_map = {
    '/sandbox/root': [('/sandbox/root/file1.jpg', 'file1.jpg')]
}
expected_file_path = '/sandbox/root/file1.jpg'


# Mock the GCS Client
@pytest.fixture
def mock_gcs_client():
    return MagicMock(spec=storage.Client)

# Mock the GCS Bucket
@pytest.fixture
def mock_gcs_bucket(mock_gcs_client):
    mock_bucket = MagicMock(spec=storage.Bucket)
    mock_gcs_client.bucket.return_value = mock_bucket
    return mock_bucket

# Use pytest.mark.parametrize to create dynamic test cases
@pytest.mark.parametrize('project_id, bucket_name', test_params)
def test_gcsuploader_init(mock_gcs_client, mock_gcs_bucket, project_id, bucket_name):
    with patch.dict(os.environ, {'GOOGLE_APPLICATION_CREDENTIALS': MOCK_CREDENTIALS_PATH}):
        uploader = GCSUploader(project_id, bucket_name, MOCK_CREDENTIALS_PATH)
        assert uploader.client == mock_gcs_client
        assert uploader.bucket_name == bucket_name
        mock_gcs_client.assert_called_once_with(project=project_id)

@pytest.mark.parametrize('project_id, bucket_name', test_params)
def test_gcsuploader_upload_to_gcs(mock_gcs_bucket, project_id, bucket_name):
    with patch.dict(os.environ, {'GOOGLE_APPLICATION_CREDENTIALS': MOCK_CREDENTIALS_PATH}):
        uploader = GCSUploader(project_id, bucket_name, MOCK_CREDENTIALS_PATH)
    
        # Mock blob and upload_from_filename method
        mock_blob = MagicMock(spec=storage.Blob)
        mock_gcs_bucket.blob.return_value = mock_blob

        # Perform the upload
        uploader.upload_to_gcs(file_path_map)

        # Assertions
        mock_gcs_bucket.assert_called_once()
        mock_blob.upload_from_filename.assert_called_once_with(expected_file_path)

@pytest.mark.parametrize('project_id, bucket_name', test_params)
def test_gcsuploader_upload_to_gcs_with_exception(mock_gcs_bucket, project_id, bucket_name):
    with patch.dict(os.environ, {'GOOGLE_APPLICATION_CREDENTIALS': MOCK_CREDENTIALS_PATH}):
        uploader = GCSUploader(project_id, bucket_name, MOCK_CREDENTIALS_PATH)
    
        # Mock blob and upload_from_filename method to raise an exception
        mock_blob = MagicMock(spec=storage.Blob)
        mock_blob.upload_from_filename.side_effect = Exception('Upload failed')
        mock_gcs_bucket.blob.return_value = mock_blob

        # Perform the upload and check that the exception is raised
        with pytest.raises(Exception, match='Upload failed'):
            uploader.upload_to_gcs(file_path_map)
