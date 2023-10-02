from setuptools import setup, find_packages

setup(
    name='uploader',
    version='1.0',
    description='To upload system files to GCS and S3',
    author='Shiv Singh',
    author_email='shivpsingh0191@gmail.com',
    packages=find_packages(),
    install_requires=[
        'boto3==1.28.57',
        'google-cloud-storage==2.11.0',
        'pytest==7.4.2',
    ],
    classifiers=[
        'Development Status :: 4 - Beta/Testing',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='uploading, GCS, S3',
    project_urls={
        'Source': 'https://github.com/shiv0191/project_uploader',
    },
)
