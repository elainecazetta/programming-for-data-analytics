import requests

url =" https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
#print(data)
print(data['northern-ireland']['events'][0])