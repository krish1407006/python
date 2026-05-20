# request module is used to make HTTP requests
import requests
# BeautifulSoup is used to parse HTML content
from bs4 import BeautifulSoup
# URL of the webpage to scrape
url = 'https://www.google.com'
# Send a GET request to the URL
response = requests.get(url)
# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
     soup = BeautifulSoup(response.text, 'html.parser')
    # Find all the search result titles
titles = soup.find_all('h3')
    # Print the titles of the search results
for title in titles:
        print(title.get_text())

else:
        print(f'Failed to retrieve the webpage. Status code: {response.status_code}')