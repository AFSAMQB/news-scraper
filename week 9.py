import tkinter as tk
import json
import os
from datetime import datetime, timedelta
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------------- DATA ----------------
FILE_PATH = "expenses.json"
WEEKLY_BUDGET = 10000


def load_expenses():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)


def save_expenses(expenses):
    with open(FILE_PATH, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expense(amount, category):
    expenses = load_expenses()
    expenses.append({
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d")
    })
    save_expenses(expenses)


def get_last_7_days():
    expenses = load_expenses()
    today = datetime.now()
    result = []

    for e in expenses:
        date = datetime.strptime(e["date"], "%Y-%m-%d")
        if today - date <= timedelta(days=7):
            result.append(e)

    return result


# ---------------- PREDICTION ----------------
def predict_week(expenses):
    if not expenses:
        return 0
    total = sum(e["amount"] for e in expenses)
    avg = total / len(expenses)
    return avg * 7


# ---------------- DETECTIVE ----------------
def categorize(category):
    c = category.lower()
    if "food" in c:
        return "Food 🍔"
    elif "travel" in c:
        return "Transport 🚗"
    elif "shop" in c:
        return "Shopping 🛍️"
    return "Other"


def find_suspect(expenses):
    summary = {}
    for e in expenses:
        cat = categorize(e["category"])
        summary[cat] = summary.get(cat, 0) + e["amount"]

    if not summary:
        return "No suspects", {}

    suspect = max(summary, key=summary.get)
    return suspect, summary


# ---------------- CHART ----------------
def show_chart(frame, expenses):
    for widget in frame.winfo_children():
        widget.destroy()

    if not expenses:
        tk.Label(frame, text="No data yet").pack()
        return

    daily = defaultdict(float)
    for e in expenses:
        daily[e["date"]] += e["amount"]

    sorted_data = sorted(daily.items(), key=lambda x: x[0])

    dates = [datetime.strptime(d, "%Y-%m-%d").strftime("%d %b") for d, _ in sorted_data]
    amounts = [a for _, a in sorted_data]

    fig, ax = plt.subplots()
    ax.bar(dates, amounts)
    ax.set_title("Last 7 Days Spending")
    ax.set_xlabel("Date")
    ax.set_ylabel("PKR")

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)


# ---------------- ANIMATION ----------------
def type_writer(label, text, i=0):
    if i < len(text):
        label.config(text=label.cget("text") + text[i])
        label.after(30, type_writer, label, text, i + 1)


def blink(label, count=0):
    if count < 6:
        current = label.cget("fg")
        new = "red" if current == "black" else "black"
        label.config(fg=new)
        label.after(300, blink, label, count + 1)


# ---------------- CRIME BOARD ----------------
def show_crime_board(root, suspect, summary):
    win = tk.Toplevel(root)
    win.title("Crime Board 🧷")
    win.geometry("300x300")

    tk.Label(win, text="🕵️ Crime Board", font=("Arial", 14)).pack(pady=10)

    for k, v in summary.items():
        tk.Label(win, text=f"{k}: {v} PKR").pack()

    tk.Label(win, text=f"\n🎯 Prime Suspect:\n{suspect}", fg="red").pack(pady=10)


# ---------------- DASHBOARD ----------------
def open_dashboard():
    root = tk.Tk()
    root.title("Budget Sleuth Dashboard")
    root.geometry("500x600")
    root.configure(bg="#1e1e1e")

    tk.Label(root, text="🕵️ Dashboard", fg="white", bg="#1e1e1e",
             font=("Arial", 16)).pack(pady=10)

    amount_entry = tk.Entry(root)
    amount_entry.pack(pady=5)
    amount_entry.insert(0, "Amount")

    category_entry = tk.Entry(root)
    category_entry.pack(pady=5)
    category_entry.insert(0, "Category")

    status = tk.Label(root, text="", bg="#1e1e1e", fg="white")
    status.pack()

    result = tk.Label(root, text="", bg="#1e1e1e", fg="white")
    result.pack()

    chart_frame = tk.Frame(root)
    chart_frame.pack(fill="both", expand=True)

    def display_chart():
        data = get_last_7_days()
        show_chart(chart_frame, data)

    def add():
        try:
            amount = float(amount_entry.get())
            category = category_entry.get()
            add_expense(amount, category)
            status.config(text="Expense Added ✅")

            display_chart()  # 🔥 REAL-TIME UPDATE

        except:
            status.config(text="Invalid Input ❌")

    def analyze():
        data = get_last_7_days()
        prediction = predict_week(data)

        result.config(text="", fg="white")

        if prediction > WEEKLY_BUDGET:
            alert = "🚨 Overspending Detected!"
            blink(result)
        else:
            alert = "All good 👍"

        message = f"Prediction: {prediction:.0f} PKR\n{alert}"
        type_writer(result, message)

    def detective():
        data = get_last_7_days()
        suspect, summary = find_suspect(data)
        show_crime_board(root, suspect, summary)

    tk.Button(root, text="Add Expense", command=add).pack(pady=5)
    tk.Button(root, text="Analyze", command=analyze).pack(pady=5)
    tk.Button(root, text="Run Detective 🕵️", command=detective).pack(pady=5)
    tk.Button(root, text="Show Chart 📊", command=display_chart).pack(pady=5)

    root.mainloop()


# ---------------- LOGIN ----------------
def open_login():
    root = tk.Tk()
    root.title("Budget Sleuth Login")
    root.geometry("300x250")

    tk.Label(root, text="🕵️ Budget Sleuth", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Email").pack()
    tk.Entry(root).pack()

    tk.Label(root, text="Password").pack()
    tk.Entry(root, show="*").pack()

    def login():
        root.destroy()
        open_dashboard()

    tk.Button(root, text="Login", command=login).pack(pady=10)

    root.mainloop()


# ---------------- MAIN ----------------
if __name__ == "__main__":
    open_login()