from setuptools import setup, find_packages

setup(
    name="sinopsis-ai",
    version="0.3.0", 
    author="Sinopsis Data, LLC", 
    author_email="hello@sinopsisai.com",
    description="A Python SDK for Sinopsis AI",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown", 
    url="https://github.com/sinopsis-ai/sinopsis-ai-sdk", 
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "boto3==1.24.28"
    ]
)