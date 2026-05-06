from flask import Flask, render_template_string, request, jsonify, send_file
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from datetime import datetime
import pandas as pd
import io

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🌍 News Scraper</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; font-family:'Poppins',sans-serif; transition:all 0.3s ease; }
        body.light { background:#f0f4f8; color:#1a1a2e; }
        body.dark { background:#1a1a2e; color:#e0e0e0; }
        nav { display:flex; justify-content:space-between; align-items:center; padding:15px 40px; background:linear-gradient(135deg,#667eea,#764ba2); color:white; box-shadow:0 4px 15px rgba(0,0,0,0.2); }
        .logo { font-size:1.5rem; font-weight:700; }
        nav button { background:rgba(255,255,255,0.2); border:2px solid white; color:white; padding:8px 20px; border-radius:25px; cursor:pointer; font-size:0.9rem; font-weight:600; }
        nav button:hover { background:white; color:#667eea; }
        .hero { text-align:center; padding:50px 20px 60px; background:linear-gradient(135deg,#667eea,#764ba2); color:white; }
        .hero h1 { font-size:2.8rem; font-weight:700; margin-bottom:10px; }
        .hero h1 span { color:#ffd700; }
        .hero p { font-size:1.1rem; opacity:0.9; }
        .container { max-width:1000px; margin:-30px auto 40px; padding:0 20px; }
        .card { background:white; border-radius:20px; padding:35px; box-shadow:0 10px 40px rgba(0,0,0,0.1); margin-bottom:25px; }
        body.dark .card { background:#16213e; }
        .input-group { margin-bottom:20px; }
        .input-group label { display:block; font-weight:600; margin-bottom:8px; color:#667eea; }
        body.dark .input-group label { color:#a78bfa; }
        .input-group input, .input-group select { width:100%; padding:12px 18px; border:2px solid #e0e0e0; border-radius:12px; font-size:0.95rem; outline:none; background:#f8f9ff; color:#1a1a2e; }
        body.dark .input-group input, body.dark .input-group select { background:#0f3460; border-color:#667eea; color:#e0e0e0; }
        .input-group input:focus, .input-group select:focus { border-color:#667eea; box-shadow:0 0 0 3px rgba(102,126,234,0.2); }
        .quick { display:flex; align-items:center; gap:10px; margin-bottom:20px; flex-wrap:wrap; }
        .quick span { font-weight:600; color:#667eea; }
        .quick button { background:linear-gradient(135deg,#667eea,#764ba2); color:white; border:none; padding:6px 18px; border-radius:20px; cursor:pointer; font-size:0.85rem; font-weight:600; }
        .quick button:hover { transform:translateY(-2px); box-shadow:0 5px 15px rgba(102,126,234,0.4); }
        .row { display:grid; grid-template-columns:1fr 1fr; gap:20px; }
        .btns { display:flex; gap:12px; flex-wrap:wrap; margin-top:10px; }
        .btn { padding:12px 25px; border:none; border-radius:12px; cursor:pointer; font-size:0.95rem; font-weight:600; display:flex; align-items:center; gap:8px; }
        .btn-scrape { background:linear-gradient(135deg,#667eea,#764ba2); color:white; flex:1; justify-content:center; }
        .btn-refresh { background:linear-gradient(135deg,#11998e,#38ef7d); color:white; }
        .btn-download { background:linear-gradient(135deg,#f093fb,#f5576c); color:white; }
        .btn:hover { transform:translateY(-2px); box-shadow:0 8px 20px rgba(0,0,0,0.2); }
        .stats { display:grid; grid-template-columns:repeat(4,1fr); gap:15px; margin-bottom:25px; }
        .stat { background:white; border-radius:15px; padding:20px; text-align:center; box-shadow:0 5px 20px rgba(0,0,0,0.08); }
        body.dark .stat { background:#16213e; }
        .stat i { font-size:1.8rem; color:#667eea; display:block; margin-bottom:8px; }
        .stat.pos i { color:#38ef7d; } .stat.neg i { color:#f5576c; } .stat.neu i { color:#ffd700; }
        .stat span { display:block; font-size:1.8rem; font-weight:700; color:#667eea; }
        .stat p { font-size:0.85rem; opacity:0.7; }
        .loading { text-align:center; padding:40px; display:none; }
        .spinner { width:50px; height:50px; border:5px solid #e0e0e0; border-top-color:#667eea; border-radius:50%; animation:spin 1s linear infinite; margin:0 auto 15px; }
        @keyframes spin { to { transform:rotate(360deg); } }
        .error { background:#fff5f5; border:2px solid #f5576c; color:#f5576c; padding:15px 20px; border-radius:12px; margin-bottom:20px; font-weight:600; display:none; }
        .news-card { background:white; border-radius:15px; padding:20px 25px; margin-bottom:15px; box-shadow:0 5px 20px rgba(0,0,0,0.07); border-left:5px solid #667eea; display:flex; justify-content:space-between; align-items:center; gap:15px; }
        body.dark .news-card { background:#16213e; }
        .news-card.pos { border-left-color:#38ef7d; } .news-card.neg { border-left-color:#f5576c; } .news-card.neu { border-left-color:#ffd700; }
        .news-card h3 { font-size:1rem; font-weight:600; margin-bottom:8px; line-height:1.4; }
        .news-card a { color:#667eea; text-decoration:none; font-size:0.85rem; font-weight:600; }
        .news-card a:hover { text-decoration:underline; }
        .badge { padding:6px 14px; border-radius:20px; font-size:0.8rem; font-weight:700; white-space:nowrap; }
        .badge.pos { background:#e8fff4; color:#11998e; } .badge.neg { background:#fff0f3; color:#f5576c; } .badge.neu { background:#fffbea; color:#f0a500; }
        @media(max-width:600px) { .row { grid-template-columns:1fr; } .stats { grid-template-columns:repeat(2,1fr); } .hero h1 { font-size:1.8rem; } .btns { flex-direction:column; } }
    </style>
</head>
<body class="light">
    <nav>
        <div class="logo">🌍 NewsScraper</div>
        <button onclick="toggleTheme()">🌙 Dark Mode</button>
    </nav>
    <div class="hero">
        <h1>Scrape News <span>Instantly</span></h1>
        <p>Enter any news website and get headlines with sentiment analysis!</p>
    </div>
    <div class="container">
        <div class="card">
            <div class="input-group">
                <label><i class="fas fa-link"></i> News Website URL</label>
                <input type="text" id="urlInput" placeholder="https://www.bbc.com/news" />
            </div>
            <div class="quick">
                <span>Quick Select:</span>
                <button onclick="setURL('https://www.bbc.com/news')">BBC</button>
                <button onclick="setURL('https://www.reuters.com')">Reuters</button>
                <button onclick="setURL('https://www.aljazeera.com')">Al Jazeera</button>
                <button onclick="setURL('https://www.dawn.com')">Dawn</button>
            </div>
            <div class="row">
                <div class="input-group">
                    <label><i class="fas fa-newspaper"></i> Category</label>
                    <select id="categoryInput">
                        <option>General</option>
                        <option>Politics</option>
                        <option>Sports</option>
                        <option>Technology</option>
                        <option>Business</option>
                        <option>Health</option>
                    </select>
                </div>
                <div class="input-group">
                    <label><i class="fas fa-globe"></i> Country</label>
                    <select id="countryInput">
                        <option>International</option>
                        <option>Pakistan</option>
                        <option>UK</option>
                        <option>USA</option>
                        <option>India</option>
                        <option>Qatar</option>
                    </select>
                </div>
            </div>
            <div class="input-group">
                <label><i class="fas fa-search"></i> Filter Headlines</label>
                <input type="text" id="searchInput" placeholder="Search headlines..." oninput="filterNews()" />
            </div>
            <div class="btns">
                <button class="btn btn-scrape" onclick="scrapeNews()"><i class="fas fa-spider"></i> Scrape News</button>
                <button class="btn btn-refresh" onclick="scrapeNews()"><i class="fas fa-sync"></i> Refresh</button>
                <button class="btn btn-download" onclick="downloadCSV()"><i class="fas fa-download"></i> Download CSV</button>
            </div>
        </div>
        <div class="stats" id="statsBar" style="display:none;">
            <div class="stat"><i class="fas fa-newspaper"></i><span id="totalCount">0</span><p>Total</p></div>
            <div class="stat pos"><i class="fas fa-smile"></i><span id="posCount">0</span><p>Positive</p></div>
            <div class="stat neu"><i class="fas fa-meh"></i><span id="neuCount">0</span><p>Neutral</p></div>
            <div class="stat neg"><i class="fas fa-frown"></i><span id="negCount">0</span><p>Negative</p></div>
        </div>
        <div class="loading" id="loading"><div class="spinner"></div><p>Scraping news... please wait!</p></div>
        <div class="error" id="errorMsg"></div>
        <div id="results"></div>
    </div>
    <script>
        let allArticles = [];
        function setURL(url) { document.getElementById("urlInput").value = url; }
        function toggleTheme() {
            document.body.classList.toggle("dark");
            document.body.classList.toggle("light");
            const btn = document.querySelector("nav button");
            btn.textContent = document.body.classList.contains("dark") ? "☀️ Light Mode" : "🌙 Dark Mode";
        }
        async function scrapeNews() {
            const url = document.getElementById("urlInput").value.trim();
            const category = document.getElementById("categoryInput").value;
            const country = document.getElementById("countryInput").value;
            if (!url) { showError("Please enter a news website URL!"); return; }
            document.getElementById("loading").style.display = "block";
            document.getElementById("results").innerHTML = "";
            document.getElementById("statsBar").style.display = "none";
            document.getElementById("errorMsg").style.display = "none";
            try {
                const res = await fetch("/scrape", { method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify({url, category, country}) });
                const data = await res.json();
                if (data.error) { showError(data.error); return; }
                allArticles = data.articles;
                displayNews(allArticles);
                updateStats(allArticles);
            } catch(e) { showError("Something went wrong! Please try again."); }
            finally { document.getElementById("loading").style.display = "none"; }
        }
        function displayNews(articles) {
            const results = document.getElementById("results");
            if (!articles.length) { results.innerHTML = '<div style="text-align:center;padding:40px;opacity:0.6;"><i class="fas fa-newspaper" style="font-size:3rem;"></i><p style="margin-top:15px;">No articles found!</p></div>'; return; }
            results.innerHTML = articles.map((a,i) => {
                const c = a.Sentiment.includes("Positive") ? "pos" : a.Sentiment.includes("Negative") ? "neg" : "neu";
                return `<div class="news-card ${c}"><div><h3>${i+1}. ${a.Headline}</h3><a href="${a.Link}" target="_blank"><i class="fas fa-external-link-alt"></i> Read Full Article</a><span style="margin-left:15px;font-size:0.8rem;opacity:0.6;">📅 ${a.Date} ⏰ ${a.Time} 🌍 ${a.Country} 📰 ${a.Category}</span></div><span class="badge ${c}">${a.Sentiment}</span></div>`;
            }).join("");
        }
        function updateStats(articles) {
            const pos = articles.filter(a => a.Sentiment.includes("Positive")).length;
            const neg = articles.filter(a => a.Sentiment.includes("Negative")).length;
            const neu = articles.filter(a => a.Sentiment.includes("Neutral")).length;
            document.getElementById("totalCount").textContent = articles.length;
            document.getElementById("posCount").textContent = pos;
            document.getElementById("negCount").textContent = neg;
            document.getElementById("neuCount").textContent = neu;
            document.getElementById("statsBar").style.display = "grid";
        }
        function filterNews() {
            const q = document.getElementById("searchInput").value.toLowerCase();
            displayNews(allArticles.filter(a => a.Headline.toLowerCase().includes(q)));
        }
        async function downloadCSV() {
            if (!allArticles.length) { showError("Please scrape news first!"); return; }
            const res = await fetch("/download/csv", { method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify({articles:allArticles}) });
            const blob = await res.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = url; a.download = "news.csv"; a.click();
        }
        function showError(msg) {
            const err = document.getElementById("errorMsg");
            err.textContent = "❌ " + msg;
            err.style.display = "block";
            document.getElementById("loading").style.display = "none";
        }
    </script>
</body>
</html>
'''

def scrape_news(source_url, category=None, country=None):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(source_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        articles = []
        for tag in soup.find_all("a", href=True):
            headline = tag.get_text().strip()
            link = tag["href"]
            if len(headline) < 20:
                continue
            if link.startswith("/"):
                from urllib.parse import urlparse
                base = urlparse(source_url)
                link = f"{base.scheme}://{base.netloc}{link}"
            score = TextBlob(headline).sentiment.polarity
            sentiment = "Positive 😊" if score > 0 else "Negative 😟" if score < 0 else "Neutral 😐"
            articles.append({
                "Headline": headline,
                "Link": link,
                "Sentiment": sentiment,
                "Date": datetime.now().strftime("%Y-%m-%d"),
                "Time": datetime.now().strftime("%H:%M"),
                "Category": category or "General",
                "Country": country or "International"
            })
        return articles[:50]
    except:
        return []

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/scrape", methods=["POST"])
def scrape():
    data = request.json
    url = data.get("url")
    category = data.get("category")
    country = data.get("country")
    if not url:
        return jsonify({"error": "Please enter a URL!"}), 400
    articles = scrape_news(url, category, country)
    if not articles:
        return jsonify({"error": "No articles found! Try another URL."}), 404
    return jsonify({"articles": articles, "total": len(articles)})

@app.route("/download/csv", methods=["POST"])
def download_csv():
    data = request.json
    articles = data.get("articles", [])
    df = pd.DataFrame(articles)
    output = io.StringIO()
    df.to_csv(output, index=False)
    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype="text/csv",
        as_attachment=True,
        download_name="news.csv"
    )

if __name__ == "__main__":
    app.run(debug=True)