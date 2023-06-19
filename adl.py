# Defining the location first and then scraping the only data which has the rating higher than '4' and has a verified tag.

import requests
from bs4 import BeautifulSoup
import json

# Define the place for scraping (e.g., 'bangalore','mumbai',etc)
place = 'bangalore'

data = []
z = 1

# Loop through the pages to scrape data
for j in range(1, 100):
    url = f"https://www.yelu.in/location/{place}/{j}"

    # Send a GET request to the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all company entries on the page
    company_list = soup.find_all('div', class_='company with_img g_0')

    # Loop through each company entry
    for company in company_list:
        # To extract information
        company_name = company.a.text.strip()
        company_address = company.find('div', class_='address').text.strip()
        company_description = company.find('div', class_='details').text.strip()
        company_link = company.h4.a['href']
        image = company.img['data-src']
        company_data = {
            'company_number': z,
            'company_name': company_name,
            'company_address': company_address,
            'company_description': company_description,
            'company_link': f'https://www.yelu.in/{company_link}',
            'company_logo': f'https://www.yelu.in/{image}'
        }

        # Check if company rating is available and higher than 4.0
        if company and company.find('div', {'class': 'rate'}):
            company_rating = company.find('div', {'class': 'rate'}).text
            if float(company_rating) > 4.0:
                company_data['company_rating'] = company_rating
            else:
                continue
        else:
            continue

        # Check if company has a verified tag
        if company and company.find('u', {'class': 'v'}):
            company_verified_tag = company.find('u', {'class': 'v'}).text.strip()
            company_data['company_verified_tag'] = company_verified_tag
        else:
            continue

        # Append the company data to the list
        data.append(company_data)
        z += 1

        # Break the loop if 1000 entries are reached
        if len(data) >= 1000:
            break

    # Break the loop if 1000 entries are reached
    if len(data) >= 1000:
        break

# Save the scraped data in JSON format
with open('scraped_data1.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Data saved successfully in scraped_data1.json")

