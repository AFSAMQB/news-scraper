import pandas as pd
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────
#   STEP 6 — CHARTS & VISUALIZATIONS
# ─────────────────────────────────────────────

# Load the saved data
df = pd.read_csv("bbc_news_final.csv")

# Add headline length column
df["Length"] = df["Headline"].str.len()

# ─────────────────────────────────────────────
#   CHART 1 — Headline Length Bar Chart
# ─────────────────────────────────────────────
plt.figure(figsize=(12, 6))
plt.bar(range(1, len(df) + 1), df["Length"], color="steelblue")
plt.title("BBC News — Headline Lengths", fontsize=16)
plt.xlabel("Headline Number", fontsize=12)
plt.ylabel("Length (characters)", fontsize=12)
plt.tight_layout()
plt.savefig("chart1_lengths.png")
plt.show()
print("✅ Chart 1 saved — chart1_lengths.png")

# ─────────────────────────────────────────────
#   CHART 2 — Top 10 Longest Headlines
# ──────────────────