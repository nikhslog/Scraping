# To crawl 20 profiles from scraped_data which is in json format.

import requests
from bs4 import BeautifulSoup
import json

cleaned_data = []

with open('scraped_data.json', 'r') as file:
    data = json.load(file)

for company_data in data[0:20]:
    company_link = company_data['company_link']
    response = requests.get(company_link)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Perform data cleaning and extraction
    cleaned_company_data = {
        'Company Number': company_data['company_number'],
        'Company Name': company_data['company_name'],
        'Company Address': company_data['company_address'],
        'Company Description': company_data['company_description'],
        'Company Link': company_link,
        'Company Logo': company_data['company_logo'],
        'Company Rating': company_data['company_rating'],
        'Company Verified Tag': company_data['company_verified_tag']
    }

    cleaned_data.append(cleaned_company_data)

# To save cleaned data to a new JSON file
with open('cleaned_data.json', 'w') as outfile:
    json.dump(cleaned_data, outfile, indent=4)
print("Data saved successfully in cleaned_data.json")

