# ============================================================
#   BBC NEWS WEB SCRAPER — Final Project
#   Course  : Advanced Python
#   Student : Shen Yi
#   Topic   : Web Scraping
# ============================================================
#
#   LIBRARIES USED:
#   • requests       — Fetch the webpage
#   • BeautifulSoup  — Extract data from HTML
#   • pandas         — Organize & analyze data
#   • schedule       — Auto-run every 10 minutes
#   • time           — Keep program running
#   • datetime       — Record scrape timestamps
# ============================================================

import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time
from datetime import datetime


# ─────────────────────────────────────────────
#   STEP 1 — FETCH THE WEBPAGE
# ─────────────────────────────────────────────
def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("✅ Page fetched successfully!")
        return response
    else:
        print(f"❌ Failed to fetch page. Status code: {response.status_code}")
        return None


# ─────────────────────────────────────────────
#   STEP 2 — EXTRACT HEADLINES & LINKS
# ─────────────────────────────────────────────
def extract_news(response):
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("a", attrs={"data-testid": "internal-link"})

    news_list = []
    for article in articles:
        headline = article.find("h2", attrs={"data-testid": "card-headline"})
        link = article.get("href")
        if headline and link:
            news_list.append({
                "Headline"  : headline.get_text().strip(),
                "Link"      : "https://www.bbc.com" + link,
                "Scraped At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

    print(f"📰 Total articles found: {len(news_list)}\n")
    return news_list


# ─────────────────────────────────────────────
#   STEP 3 — DISPLAY IN TERMINAL
# ─────────────────────────────────────────────
def display_news(news_list):
    for i, news in enumerate(news_list, 1):
        print(f"{i}. {news['Headline']}")
        print(f"   🔗 {news['Link']}\n")


# ─────────────────────────────────────────────
#   STEP 4 — ANALYZE WITH PANDAS
# ─────────────────────────────────────────────
def analyze_news(df):
    print("=" * 50)
    print("📊 QUICK ANALYSIS")
    print("=" * 50)
    print(f"  Total Headlines  : {len(df)}")
    print(f"  Longest Headline : {df['Headline'].str.len().max()} characters")
    print(f"  Shortest Headline: {df['Headline'].str.len().min()} characters")
    print(f"  Average Length   : {df['Headline'].str.len().mean():.1f} characters")
    print("=" * 50 + "\n")


# ─────────────────────────────────────────────
#   STEP 5 — SAVE TO CSV & EXCEL
# ─────────────────────────────────────────────
def save_data(df):
    df.to_csv("bbc_news_final.csv", index=False)
    print("✅ Saved to bbc_news_final.csv!")
    df.to_excel("bbc_news_final.xlsx", index=False)
    print("✅ Saved to bbc_news_final.xlsx!")


# ─────────────────────────────────────────────
#   MAIN SCRAPING FUNCTION
# ─────────────────────────────────────────────
def scrape_bbc_news():
    print("\n" + "=" * 50)
    print(f"  ⏰ Scrape started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50 + "\n")

    url = "https://www.bbc.com/news"

    # Run all steps
    response = fetch_page(url)
    if response:
        news_list = extract_news(response)
        display_news(news_list)
        df = pd.DataFrame(news_list)
        analyze_news(df)
        save_data(df)
        print(f"⏳ Next scrape in 10 minutes...\n")


# ─────────────────────────────────────────────
#   RUN IMMEDIATELY + AUTO EVERY 10 MINUTES
# ─────────────────────────────────────────────
scrape_bbc_news()

schedule.every(10).minutes.do(scrape_bbc_news)

while True:
    schedule.run_pending()
    time.sleep(1)