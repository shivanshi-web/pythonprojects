import csv
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

expenses = []

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    expenses.append({'date': date, 'category': category, 'amount': amount, 'description': description})

def view_expenses():
    for e in expenses:
        print(f"{e['date']} | {e['category']} | ₹{e['amount']} | {e['description']}")

def show_summary():
    total = sum(e['amount'] for e in expenses)
    print(f"Total Spent: ₹{total:.2f}")
    summary = defaultdict(float)
    for e in expenses:
        summary[e['category']] += e['amount']
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt:.2f}")

def save_to_csv(filename='expenses.csv'):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        writer.writerows(expenses)

def load_from_csv(filename='expenses.csv'):
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            expenses.clear()
            for row in reader:
                row['amount'] = float(row['amount'])
                expenses.append(row)
    except FileNotFoundError:
        print("File not found.")

def plot_category_pie():
    summary = defaultdict(float)
    for e in expenses:
        summary[e['category']] += e['amount']
    labels, values = zip(*summary.items())
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title('Spending by Category')
    plt.show()

def plot_daily_expense_bar():
    daily = defaultdict(float)
    for e in expenses:
        daily[e['date']] += e['amount']
    dates = sorted(daily)
    values = [daily[d] for d in dates]
    plt.bar(dates, values)
    plt.title("Daily Expenses")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

while True:
    print("\n1. Add\n2. View\n3. Summary\n4. Save\n5. Load\n6. Pie\n7. Bar\n8. Exit")
    ch = input("Choice: ")
    if ch == '1': add_expense()
    elif ch == '2': view_expenses()
    elif ch == '3': show_summary()
    elif ch == '4': save_to_csv()
    elif ch == '5': load_from_csv()
    elif ch == '6': plot_category_pie()
    elif ch == '7': plot_daily_expense_bar()
    elif ch == '8': break