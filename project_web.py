# ============================================================
#   BBC NEWS WEB SCRAPER — Final Project
#   Course  : Advanced Python
#   Student : Shen Yi
#   Topic   : Web Scraping
# ============================================================
#
#   LIBRARIES USED:
#   • requests        — Fetch the webpage
#   • BeautifulSoup   — Extract data from HTML
#   • pandas          — Organize & analyze data
#   • matplotlib      — Create charts & visualizations
#   • schedule        — Auto-run every 10 minutes
#   • time            — Keep program running
#   • datetime        — Record scrape timestamps
# ============================================================

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import schedule
import time
from datetime import datetime


# ─────────────────────────────────────────────
#   STEP 1 — FETCH THE WEBPAGE
# ─────────────────────────────────────────────
def fetch_page(url):
    print("🌐 Fetching BBC News page...")
    response = requests.get(url)
    if response.status_code == 200:
        print("✅ Page fetched successfully!\n")
        return response
    else:
        print(f"❌ Failed to fetch page. Status code: {response.status_code}")
        return None


# ─────────────────────────────────────────────
#   STEP 2 — EXTRACT HEADLINES & LINKS
# ─────────────────────────────────────────────
def extract_news(response):
    print("🔍 Extracting headlines and links...")
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
    print("=" * 55)
    print("📋 ALL HEADLINES & LINKS")
    print("=" * 55)
    for i, news in enumerate(news_list, 1):
        print(f"{i}. {news['Headline']}")
        print(f"   🔗 {news['Link']}\n")


# ─────────────────────────────────────────────
#   STEP 4 — ANALYZE WITH PANDAS
# ─────────────────────────────────────────────
def analyze_news(df):
    print("=" * 55)
    print("📊 QUICK ANALYSIS")
    print("=" * 55)
    print(f"  Total Headlines   : {len(df)}")
    print(f"  Longest Headline  : {df['Headline'].str.len().max()} characters")
    print(f"  Shortest Headline : {df['Headline'].str.len().min()} characters")
    print(f"  Average Length    : {df['Headline'].str.len().mean():.1f} characters")
    print("=" * 55 + "\n")


# ─────────────────────────────────────────────
#   STEP 5 — SAVE TO CSV & EXCEL
# ─────────────────────────────────────────────
def save_data(df):
    print("💾 Saving data...")
    df.to_csv("bbc_news_final.csv", index=False)
    print("✅ Saved to bbc_news_final.csv!")
    df.to_excel("bbc_news_final.xlsx", index=False)
    print("✅ Saved to bbc_news_final.xlsx!\n")


# ─────────────────────────────────────────────
#   STEP 6 — CHARTS & VISUALIZATIONS
# ─────────────────────────────────────────────
def create_charts(df):
    print("📈 Creating charts...")
    df["Length"] = df["Headline"].str.len()

    # Chart 1 — Headline Length Bar Chart
    plt.figure(figsize=(12, 6))
    plt.bar(range(1, len(df) + 1), df["Length"], color="steelblue")
    plt.title("BBC News — Headline Lengths", fontsize=16)
    plt.xlabel("Headline Number", fontsize=12)
    plt.ylabel("Length (characters)", fontsize=12)
    plt.tight_layout()
    plt.savefig("chart1_lengths.png")
    plt.show()
    print("✅ Chart 1 saved — chart1_lengths.png")

    # Chart 2 — Top 10 Longest Headlines
    top10 = df.nlargest(10, "Length")
    plt.figure(figsize=(12, 6))
    plt.barh(top10["Headline"].str[:40] + "...", top10["Length"], color="tomato")
    plt.title("BBC News — Top 10 Longest Headlines", fontsize=16)
    plt.xlabel("Length (characters)", fontsize=12)
    plt.tight_layout()
    plt.savefig("chart2_top10.png")
    plt.show()
    print("✅ Chart 2 saved — chart2_top10.png")

    # Chart 3 — Headline Length Distribution
    plt.figure(figsize=(8, 5))
    plt.hist(df["Length"], bins=10, color="mediumseagreen", edgecolor="black")
    plt.title("BBC News — Headline Length Distribution", fontsize=16)
    plt.xlabel("Length (characters)", fontsize=12)
    plt.ylabel("Number of Headlines", fontsize=12)
    plt.tight_layout()
    plt.savefig("chart3_distribution.png")
    plt.show()
    print("✅ Chart 3 saved — chart3_distribution.png\n")


# ─────────────────────────────────────────────
#   MAIN SCRAPING FUNCTION
# ─────────────────────────────────────────────
def scrape_bbc_news():
    print("\n" + "=" * 55)
    print(f"  ⏰ Scrape Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 55 + "\n")

    url = "https://www.bbc.com/news"

    # Run all steps
    response = fetch_page(url)
    if response:
        news_list = extract_news(response)
        display_news(news_list)
        df = pd.DataFrame(news_list)
        analyze_news(df)
        save_data(df)
        create_charts(df)

    print("🎉 All done!")
    print(f"⏳ Next scrape in 10 minutes...\n")


# ─────────────────────────────────────────────
#   RUN IMMEDIATELY + AUTO EVERY 10 MINUTES
# ─────────────────────────────────────────────
scrape_bbc_news()

schedule.every(10).minutes.do(scrape_bbc_news)

while True:
    schedule.run_pending()
    time.sleep(1)