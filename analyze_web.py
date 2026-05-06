import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the webpage
url = "https://www.bbc.com/news"
response = requests.get(url)

# Step 2: Parse with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract headlines
headlines = soup.find_all("h2")

# Step 4: Store in a list
news_list = []
for headline in headlines:
    text = headline.get_text().strip()
    if text:
        news_list.append(text)

# Step 5: Create pandas DataFrame
df = pd.DataFrame(news_list, columns=["Headline"])

# Step 6: Analyze
print(f"📊 Quick Analysis:\n")
print(f"Total Headlines  : {len(df)}")
print(f"Longest Headline : {df['Headline'].str.len().max()} characters")
print(f"Shortest Headline: {df['Headline'].str.len().min()} characters")
print(f"Average Length   : {df['Headline'].str.len().mean():.1f} characters")

# Step 7: Save to CSV & Excel
df.to_csv("bbc_news.csv", index=False)
print("\n✅ Saved to bbc_news.csv!")
df.to_excel("bbc_news.xlsx", index=False)
print("✅ Saved to bbc_news.xlsx!")