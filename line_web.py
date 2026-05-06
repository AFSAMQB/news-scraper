import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the webpage
url = "https://www.bbc.com/news"
response = requests.get(url)

# Step 2: Parse with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract headlines + links together
articles = soup.find_all("a", attrs={"data-testid": "internal-link"})

# Step 4: Store in a list
news_list = []
for article in articles:
    headline = article.find("h2", attrs={"data-testid": "card-headline"})
    link = article.get("href")
    if headline and link:
        news_list.append({
            "Headline": headline.get_text().strip(),
            "Link": "https://www.bbc.com" + link
        })

# Step 5: Display in terminal
print(f"✅ Total articles found: {len(news_list)}\n")
for i, news in enumerate(news_list, 1):
    print(f"{i}. {news['Headline']}")
    print(f"   🔗 {news['Link']}\n")

# Step 6: Save to CSV & Excel
df = pd.DataFrame(news_list)
df.to_csv("bbc_news_with_links.csv", index=False)
print("✅ Saved to bbc_news_with_links.csv!")
df.to_excel("bbc_news_with_links.xlsx", index=False)
print("✅ Saved to bbc_news_with_links.xlsx!")