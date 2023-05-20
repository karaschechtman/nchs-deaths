import boto3
import numpy as np
import os
import requests

# Request archive.org NVSS metadata 
nvss = "https://data.cdc.gov/api/views/r8kw-7aab/rows.csv?accessType=DOWNLOAD"
response = requests.get("http://web.archive.org/cdx/search/cdx?url=%s" % nvss).content.decode('utf-8')

# Get all the CSV urls
OK = '200'
data_ = response.split(" ")[:-1]
archived_url_data = np.array(data_).reshape(int(len(data_)/6),6)
archived_urls = {}

archived_url_format = 'http://web.archive.org/web/{timestamp}/%s' % nvss
for url_data in archived_url_data:
  if url_data[4] == OK:
    timestamp = url_data[1]
    archived_urls[timestamp]=archived_url_format.replace("{timestamp}",timestamp)

# Upload the files to S3
session = boto3.Session(
    aws_access_key_id=os.environ["S3_KEY"],
    aws_secret_access_key=os.environ["S3_PRIVATE_KEY"]
)
s3 = session.client('s3')
for date in archived_urls.keys():
  csv_text = requests.get(archived_urls[date],allow_redirects=True).content
  s3.put_object(Body=csv_text,Bucket='nvss-deaths',Key='%s.csv' % date)