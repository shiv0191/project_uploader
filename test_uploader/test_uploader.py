import os
import pytest
import unittest.mock
from unittest.mock import MagicMock, patch
from uploader.uploader import Uploader, S3Uploader, GCSUploader

# Define test parameters
S3_BUCKET_NAME = 's3_bucket_name'
AWS_ACCESS_KEY_ID = 'aws_access_key_id'
AWS_SECRET_ACCESS_KEY = 'aws_secret_access_key'
GCS_PROJECT_ID = 'gcs_project_id'
GCS_BUCKET_NAME = 'gcs_bucket_name'
GCS_CREDENTIALS_FILE_PATH = 'gcs_credentials_file_path'
S3_ALLOWED_EXTENSIONS = [".jpg", ".png"]
GCS_ALLOWED_EXTENSIONS = [".doc", ".docx", ".csv", ".pdf"]
SANDBOX_ROOT = '/sandbox/root'

# Mock the S3Uploader and GCSUploader classes
@pytest.fixture
def mock_s3_uploader():
    return MagicMock(spec=S3Uploader)

@pytest.fixture
def mock_gcs_uploader():
    return MagicMock(spec=GCSUploader)

# Mock os.walk and os.path.join
@pytest.fixture
def mock_os_walk():
    with patch('os.walk') as mock_walk:
        mock_walk.return_value = [(SANDBOX_ROOT, [], ['file1.jpg'])]
        yield mock_walk

@pytest.fixture
def mock_os_path_join():
    with patch('os.path.join') as mock_join:
        mock_join.return_value = os.path.join(SANDBOX_ROOT, 'file1.jpg')
        yield mock_join

# Test Uploader initialization
def test_uploader_init(mock_s3_uploader, mock_gcs_uploader):
    uploader = Uploader(
        S3_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,
        GCS_PROJECT_ID, GCS_BUCKET_NAME, GCS_CREDENTIALS_FILE_PATH,
    )

    assert uploader.s3_uploader == mock_s3_uploader
    assert uploader.gcs_uploader == mock_gcs_uploader

# Test Uploader file_dir_map method
def test_uploader_file_dir_map(mock_os_walk, mock_os_path_join):
    uploader = Uploader(
        S3_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,
        GCS_PROJECT_ID, GCS_BUCKET_NAME, GCS_CREDENTIALS_FILE_PATH
    )

    file_dir_map = uploader.file_dir_map(SANDBOX_ROOT)

    assert isinstance(file_dir_map, dict)
    assert 's3_files' in file_dir_map
    assert 'gcs_files' in file_dir_map
    assert file_dir_map['s3_files'] == {SANDBOX_ROOT: [(os.path.join(SANDBOX_ROOT, 'file1.jpg'), 'file1.jpg')]}
    assert file_dir_map['gcs_files'] == {SANDBOX_ROOT: [(os.path.join(SANDBOX_ROOT, 'file1.jpg'), 'file1.jpg')]}

# Test Uploader has_extension method
def test_uploader_has_extension():
    uploader = Uploader(
        S3_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,
        GCS_PROJECT_ID, GCS_BUCKET_NAME, GCS_CREDENTIALS_FILE_PATH
    )

    assert uploader.has_extension('file.jpg', S3_ALLOWED_EXTENSIONS) is True
    assert uploader.has_extension('file.txt', S3_ALLOWED_EXTENSIONS) is False

# Test Uploader auto_upload method
def test_uploader_auto_upload(mock_s3_uploader, mock_gcs_uploader, mock_os_walk, mock_os_path_join):
    uploader = Uploader(
        S3_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,
        GCS_PROJECT_ID, GCS_BUCKET_NAME, GCS_CREDENTIALS_FILE_PATH,
        s3_allowed_extensions=S3_ALLOWED_EXTENSIONS, gcs_allowed_extensions=GCS_ALLOWED_EXTENSIONS,
    )

    result = uploader.auto_upload(SANDBOX_ROOT)

    assert result is None
    mock_s3_uploader.upload_to_s3.assert_called_once()
    mock_gcs_uploader.upload_to_gcs.assert_called_once()
