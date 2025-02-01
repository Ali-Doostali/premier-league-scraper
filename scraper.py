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
# print(headers)

# Extract data from the body section of the table (tbody)
tbody = table.find("tbody")
body_rows = tbody.findAll("tr")

# Initialize a list to store the table data
table_data = []

# Append the headers only once as the first row in the table data
table_data.append(headers)

# Iterate through the rows and extract data
for row in body_rows:
    cells = row.findAll("td")
    row_data = [cell.text.strip() for cell in cells]  # Get text directly from <td>
    table_data.append(row_data)

# Print to verify data extraction
for row in table_data:
    print(row)