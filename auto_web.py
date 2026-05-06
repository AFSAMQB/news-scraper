import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time
from datetime import datetime

# ✅ Scraping function
def scrape_bbc_news():
    print(f"\n⏰ Scraping started at: {datetime.now().strftime('%H:%M:%S')}")

    # Fetch the webpage
    url = "https://www.bbc.com/news"
    response = requests.get(url)

    # Parse with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract headlines + links
    articles = soup.find_all("a", attrs={"data-testid": "internal-link"})

    news_list = []
    for article in articles:
        headline = article.find("h2", attrs={"data-testid": "card-headline"})
        link = article.get("href")
        if headline and link:
            news_list.append({
                "Headline": headline.get_text().strip(),
                "Link": "https://www.bbc.com" + link,
                "Scraped At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

    # Display in terminal
    print(f"✅ Total articles found: {len(news_list)}\n")
    for i, news in enumerate(news_list, 1):
        print(f"{i}. {news['Headline']}")
        print(f"   🔗 {news['Link']}\n")

    # Save to CSV & Excel
    df = pd.DataFrame(news_list)
    df.to_csv("bbc_news_auto.csv", index=False)
    df.to_excel("bbc_news_auto.xlsx", index=False)
    print("✅ Data saved successfully!")
    print(f"⏳ Next scrape in 1 minutes...\n")

# ✅ Run immediately once
scrape_bbc_news()

# ✅ Then auto run every 10 min
schedule.every(1).minutes.do(scrape_bbc_news)

while True:
    schedule.run_pending()
    time.sleep(1)