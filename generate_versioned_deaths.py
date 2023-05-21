import boto3
import pandas as pd
import os
from datetime import datetime
from io import StringIO

# Connect to s3
session = boto3.Session(
    aws_access_key_id=os.environ["S3_KEY"],
    aws_secret_access_key=os.environ["S3_PRIVATE_KEY"]
)
s3 = session.client('s3')

# Construct versioned weekly deaths
filenames = sorted(
    [el['Key'] for el in s3.list_objects(Bucket='nvss-deaths')['Contents'] if not el['Key'].startswith('runs/')]
)

dfs = []
for el in filenames:
    f = StringIO(s3.get_object(Bucket='nvss-deaths',
                               Key=el)
                 ['Body'].read().decode('utf-8'))
    df = pd.read_csv(f)
    # capitalization convention changes in Jan 2021
    df['Group'] = df['Group'].str.lower()
    df = df[df['Group'] == 'by week']
    dfs.append(df)
    
deaths = pd.concat(dfs, ignore_index=True)

# Save the monster dataframe to s3
filename = 'runs/' + datetime.now().strftime('%Y%m%d%H%M%S') + '.csv'
csv_buffer = StringIO()
deaths.to_csv(csv_buffer)
s3.put_object(Bucket='nvss-deaths',
              Key=filename,
              Body=csv_buffer.getvalue())
