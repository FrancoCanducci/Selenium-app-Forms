import requests
from bs4 import BeautifulSoup

# Define the URL of the website to scan
url = "https://example.com"

# Define the data to be submitted to the form
data = {
    "username": "john.doe",
    "password": "password123",
    "email": "john.doe@example.com"
}

# Make a GET request to the website and get the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the form element and its action URL
form = soup.find("form")
action_url = form["action"]

# Add the form action URL to the base URL if it's a relative URL
if not action_url.startswith("http"):
    action_url = url + action_url

# Make a POST request to the action URL with the form data
response = requests.post(action_url, data=data)

# Print the response content
print(response.content)
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status