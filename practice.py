import json, csv
from pathlib import Path
from datetime import date

DATA_FILE = Path('expenses.json')

def load_expenses():
    try:
        return json.loads(DATA_FILE.read_text())
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: data file corrupted")
        return []
def save_expenses(expenses):
    DATA_FILE.write_text(json.dumps(expenses, indent=2))

def add_expenses(amount, category, description):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError('Amount must be positive')
    except ValueError as e:
        print(f"Invalid amount: {e}")
        return None
    expenses = load_expenses()
    expense = {
        'id': len(expenses) + 1,
        'amount': amount,
        'category': category,
        'description': description,
        'date': str(date.today())
    }
    expenses.append(expense)
    save_expenses(expenses)

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    print(f"{'-' * 50 }")
    for e in expenses:
        print(
    f"{e['id']:>3} | {e['date']} | "
    f"{e['category']:12} | "
    f"PKR {e['amount']:>8.2f} | "
    f"{e['description']}"
)
    print(f"{'-' * 50 }")

def total_by_category():
    expenses = load_expenses()
    totals = {}
    for e in expenses:
        cat = e['category']
        totals[cat] = totals.get(cat, 0) + e['amount']
    return dict(sorted(totals.items(), key=lambda x: x[1], reverse=True))

def monthly_summary():
    expenses = load_expenses()
    total = sum(e['amount'] for e in expenses)
    by_cat = total_by_category()
    print(f"\n=== Monthly Summary ===")
    print(f"Total Spent: PKR {total:.2f}")
    print(f"\nBy Category:")
    for cat, amt in by_cat.items():
        pct = (amt / total * 100) if total else 0
        print(f"{cat:12} | PKR {amt:>8.2f} | {pct:>5.1f}%")

def export_csv(filename = 'report.csv'):
    expenses = load_expenses()
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'amount', 'category', 'description', 'date'])
        writer.writeheader()
        writer.writerows(expenses)
        print(f"{'-' * 50 }")

add_expenses(500, 'Food', 'Groceries')
add_expenses(200, 'Transport', 'Bus-fare')
monthly_summary()
export_csv()