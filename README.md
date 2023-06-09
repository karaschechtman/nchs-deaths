# Info

Scripts to generate versioned NCHS COVID-19 death data and notebook for analysis of NCHS data's use in the new CDC COVID-19 dashboard following expiry of the PHE. Further details and background can be found in the review document [here](https://docs.google.com/document/d/e/2PACX-1vS3QT5AzW28tmqyMJtXIpYbFewJilLIPg7YbXwMDne3ql8HY9UTN0PxAUxMNwJk3WD_f3uN3DJj4nEE/pub). 

# Contents

## Scripts
- `get_archival_nchs_data.py`: Downloads versioned NCHS death data from archive.org and saves to s3
- `get_nchs_data.py`: Daily process that gets today's NCHS death data from CDC and saves to s3
- `generate_versioned_deaths.py`: Daily process that generates a file with versioned weekly deaths by date of death

## Notebooks
- `percent_covid_associated_deaths.ipynb`: Analysis of versioned percent of total deaths that are COVID-19 associated deaths
