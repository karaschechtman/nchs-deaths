import boto3
import requests
import os
from datetime import datetime

# Get the data
URL = "https://data.cdc.gov/api/views/r8kw-7aab/rows.csv?accessType=DOWNLOAD"
data = requests.get(URL).content

# Upload to s3
keys = os.environ["S3"].splitlines()
session = boto3.Session(
	aws_access_key_id=keys.[0].strip(),
	aws_secret_access_key=keys[1].strip()
)

s3 = session.client('s3')
filename = datetime.now().strftime('%Y%m%d%H%M%S') + '.csv'
s3.put_object(Body=data,Bucket='nvss-deaths',Key=filename)
