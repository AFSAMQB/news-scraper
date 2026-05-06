"""import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage
url = "https://www.bbc.com/news"
response = requests.get(url)

# Step 2: Check if it worked
if response.status_code == 200:
    print("✅ Page fetched successfully!")
else:
    print("❌ Something went wrong:", response.status_code)"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the webpage
url = "https://www.bbc.com/news"
response = requests.get(url)

# Step 2: Parse the page with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Find all headlines
#headlines = soup.find_all("h2")
articles = soup.find_all("a", attrs={"data-testid": "internal-link"})

news_list = []
for article in articles:
    headline = article.find("h2", attrs={"data-testid": "card-headline"})
    link = article.get("href")
    if headline and link:
        news_list.append({
            "Headline": headline.get_text().strip(),
            "Link": "https://www.bbc.com" + link
        })

# Step 4: Display them


for i, news in enumerate(news_list, 1):
    print(f"{i}. {news['Headline']}")
    print(f"   🔗 {news['Link']}\n")

# Pandas Analysis
df = pd.DataFrame(news_list)
print(f"\n📊 Quick Analysis:")
print(f"Total Headlines: {len(df)}")
print(f"Longest Headline: {df['Headline'].str.len().max()} characters")
print(f"Shortest Headline: {df['Headline'].str.len().min()} characters")
print(f"Average Length: {df['Headline'].str.len().mean():.1f} characters")

# Save files
df.to_csv("bbc_news.csv", index=False)
print("\n✅ Saved to bbc_news.csv!")
df.to_excel("bbc_news.xlsx", index=False)
print("✅ Saved to bbc_news.xlsx!")