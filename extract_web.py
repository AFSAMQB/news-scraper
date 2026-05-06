import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage
url = "https://www.bbc.com/news"
response = requests.get(url)

# Step 2: Parse with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract headlines
headlines = soup.find_all("h2")

# Step 4: Display headlines
print(f"✅ Total headlines found: {len(headlines)}\n")
for i, headline in enumerate(headlines, 1):
    print(f"{i}. {headline.get_text().strip()}")