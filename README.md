# Uploader Library

The Uploader library provides a convenient way to upload system files to both Google Cloud Storage (GCS) and Amazon S3. This library is designed to simplify the process of uploading files to cloud storage services with ease.

## Features

- Upload files to Google Cloud Storage (GCS).
- Upload files to Amazon S3.


## Usage

You can use the Uploader library in the following ways:

### Using `run_uploader.py`

1. Make changes to `config.py`:

    - Set the values of `s3_bucket_name`
    - Set the values of `aws_access_key_id`
    - Set the values of `aws_secret_access_key`
    - Set the values of `gcs_project_id`
    - Set the values of `gcs_bucket_name`
    - Set the values of `gcs_credentials_file_path`
    - Set the values of `s3_allowed_extensions`
    - Set the values of `gcs_allowed_extensions`

2. Make changes to `run_uploader.py`:

    - Add the value of `root_dir_name` to specify the directory from which to upload files.

3. In your command prompt or terminal, use the following command to run it:

   ```bash
   python run_uploader.py
   ```

### Installation Method Using pip

You can install the Uploader library using pip. Open your terminal or command prompt and run the following command:

```bash
pip install uploader
```
To use the Uploader library in your code, follow these steps:

1. Import the `Uploader` class from the `uploader.uploader` module:

   ```python
   from uploader.uploader import Uploader
   ```

2. Instantiate the `Uploader` class in your code:

   ```python
   uploader = Uploader(
       s3_bucket_name='your_s3_bucket_name',
       aws_access_key_id='your_aws_access_key_id',
       aws_secret_access_key='your_aws_secret_access_key',
       gcs_project_id='your_gcs_project_id',
       gcs_bucket_name='your_gcs_bucket_name',
       gcs_credentials_file_path='path_to_your_gcs_credentials_file.json'
   )
   ```

   Make sure to set the configurations and folder paths as needed for your use case.

3. Use the `uploader` object to perform file uploads to the cloud storage services.

### Example

For an example of how to use the Uploader library, refer to the `run_uploader.py` file in this repository.

### Note

It is recommended to use a virtual environment (virtualenv) when working with Python libraries to isolate dependencies and avoid conflicts with other projects.

You can customize and expand upon this content to provide more detailed usage instructions and information about your library.

## Configuration

The Runner script uses the configuration from `config.py`. Make sure to update this file with your specific settings. The configuration should look like this:

```python
# config.py

uploader_config = {
    's3_bucket_name': 'your-s3-bucket',
    'aws_access_key_id': 'your-aws-access-key-id',
    'aws_secret_access_key': 'your-aws-secret-access-key',
    'gcs_project_id': 'your-gcs-project-id',
    'gcs_bucket_name': 'your-gcs-bucket',
    'gcs_credentials_file_path': 'path-to-your-gcs-credentials-file',
    's3_allowed_extensions': ['.jpg', '.png'],
    'gcs_allowed_extensions': ['.doc', '.pdf'],
    'root_dir_name': '/path/to/your/files'  # Replace with the directory you want to upload
}
```

## Dependencies

The Uploader library has the following dependencies:

- `boto3==1.28.57`
- `google-cloud-storage==2.11.0`
- `pytest==7.4.2`

You can install these dependencies using pip.

## Testing

### Test Uploader

The `test_uploader` folder contains test files and scripts for testing the functionality of the Uploader package. These tests ensure that the package is working as expected and help maintain its reliability.

#### Running Tests

To run the tests located in the `test_uploader` folder, follow these steps:

1. Make sure you have set up your virtual environment and installed the required dependencies as mentioned in the installation instructions.

2. Navigate to the project root directory.

3. Execute the following command to run the tests:

   ```bash
   pytest test_uploader/


## Issues and Contributions

If you encounter any issues or have suggestions for improvements, please open an issue on the [GitHub repository](https://github.com/shiv0191/project_uploader).

Happy uploading!
