import boto3
import requests
import os
from datetime import datetime

# Get the data
URL = "https://data.cdc.gov/api/views/r8kw-7aab/rows.csv?accessType=DOWNLOAD"
data = requests.get(URL).content

# Upload to s3
session = boto3.Session(
	aws_access_key_id=os.environ["S3_KEY"],
	aws_secret_access_key=os.environ["S3_PRIVATE_KEY"]
)

s3 = session.client('s3')
filename = datetime.now().strftime('%Y%m%d%H%M%S') + '.csv'
s3.put_object(Body=data,Bucket='nvss-deaths',Key=filename)
