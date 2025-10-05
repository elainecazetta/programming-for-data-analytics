# Author: Elaine Cazetta

# This program prints out the dates of the bank holidays that happen in northern Ireland:

# import requests

# url ="https://www.gov.uk/bank-holidays.json"
# response = requests.get(url)
# data = response.json()

#for event in data['northern-ireland']['events']:
    #print(event['date'], "-", event['title'])

# Extra marks:
# Modify the program to print the bank holidays that are unique to northern Ireland:

import requests

url ="https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

# Get titles for England & Wales and Scotland:
england_titles = {event['title'] for event in data['england-and-wales']['events']}
scotland_titles = {event['title'] for event in data['scotland']['events']}

# Northern Ireland events:
ni_events = data['northern-ireland']['events']

print("Bank holidays unique to Northern Ireland:")
for event in ni_events:
    title = event['title']
    date = event['date']
    if title not in england_titles and title not in scotland_titles:
        print(f"{date} - {title}")