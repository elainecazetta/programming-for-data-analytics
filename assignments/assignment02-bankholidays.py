# This program prints out the dates of the bank holidays that happen in northern Ireland.
# Author: Elaine Cazetta

import requests

url ="https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

for event in data['northern-ireland']['events']:
    print(event['date'], "-", event['title'])