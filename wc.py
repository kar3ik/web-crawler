import requests
from bs4 import BeautifulSoup

def web_crawler(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all anchor tags in the HTML
        anchor_tags = soup.find_all('a')

        # Extract the URLs from the anchor tags
        urls = [a['href'] for a in anchor_tags if 'href' in a.attrs]

        # Print the extracted URLs
        for url in urls:
            print(url)
    else:
        print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")

# Example usage
input_url = input("Enter the URL: ")
web_crawler(input_url)

