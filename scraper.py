import requests
from bs4 import BeautifulSoup

url = "https://www.skysports.com/premier-league-table"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#find the table
table = soup.find("table")

#Find the header section of the table (thead)
thead = table.find("thead")
header_row = thead.find("tr")

# Extract column names from the header row, but only get text from <span> tags
headers = [header.find("span").text.strip() if header.find("span") else header.text.strip() for header in header_row.findAll("th")]

# Print headers to verify
print(headers)