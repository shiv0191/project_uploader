import os
import boto3
import pytest
from unittest.mock import MagicMock, patch
from uploader.s3uploader import S3Uploader

DEFAULT_BUCKET_NAME = "s3-bucket-name"
DEFAULT_AWS_ACCESS_KEY_ID = "aws_access_key_id"
DEFAULT_AWS_SECRET_ACCESS_KEY = "aws_secret_access_key"

file_path_map = {
    'root/path': [
        ('root/path/xyz.jpg', 'path/xyz.jpg'),
    ]
}

def test_s3uploader_init():
    with patch('boto3.client') as mock_boto3_client:
        # Mock the S3 client
        mock_s3_client = MagicMock()
        mock_boto3_client.return_value = mock_s3_client

        uploader = S3Uploader(DEFAULT_BUCKET_NAME, DEFAULT_AWS_ACCESS_KEY_ID, DEFAULT_AWS_SECRET_ACCESS_KEY)
        assert uploader.bucket_name == DEFAULT_BUCKET_NAME
        mock_s3_client.assert_called_once_with('s3', aws_access_key_id=DEFAULT_AWS_ACCESS_KEY_ID, aws_secret_access_key=DEFAULT_AWS_SECRET_ACCESS_KEY)

def test_s3uploader_upload_to_s3():
    with patch('boto3.client') as mock_boto3_client:
        # Mock the S3 client
        mock_s3_client = MagicMock()
        mock_boto3_client.return_value = mock_s3_client

        uploader = S3Uploader(DEFAULT_BUCKET_NAME, DEFAULT_AWS_ACCESS_KEY_ID, DEFAULT_AWS_SECRET_ACCESS_KEY)

        # Perform the upload
        uploader.upload_to_s3(file_path_map)

        # Assertions
        mock_s3_client.upload_file.assert_called_once()

def test_s3uploader_upload_to_s3_with_exception():
    with patch('boto3.client') as mock_boto3_client:
        # Mock the S3 client
        mock_s3_client = MagicMock()
        mock_boto3_client.return_value = mock_s3_client

        uploader = S3Uploader(DEFAULT_BUCKET_NAME, DEFAULT_AWS_ACCESS_KEY_ID, DEFAULT_AWS_SECRET_ACCESS_KEY)

        # Mock the S3 client's upload_file method to raise an exception
        mock_s3_client.upload_file.side_effect = Exception('Upload failed')

        # Perform the upload and check that the exception is raised
        with pytest.raises(Exception, match='Upload failed'):
            uploader.upload_to_s3(file_path_map)
