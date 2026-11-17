"""Generate a realistic, deliberately messy sales CSV for practice.

Run once:  python make_messy_data.py
Output:    messy_sales.csv

Messy on purpose (just like real client files):
- column names with spaces / capitals
- city and product typed in many ways (Delhi, delhi, " DELHI ")
- dates in 3 different formats
- amounts like "N/A", "₹1,200", "1,200"
- missing customer names
- duplicate rows
"""
import random
from datetime import datetime, timedelta

import pandas as pd

random.seed(42)

CITIES = ["Delhi", "Mumbai", "Bangalore", "Pune", "Jaipur"]
PRODUCTS = ["Shirt", "Shoes", "Watch", "Bag", "Headphones"]
NAMES = ["Amit", "Neha", "Rahul", "Priya", "Sana", "Karan", None, ""]
DATE_FORMATS = ["%d-%m-%Y", "%Y/%m/%d", "%d %b %Y"]

rows = []
for i in range(1, 301):
    city = random.choice(CITIES)
    product = random.choice(PRODUCTS)
    amount = random.randint(200, 5000)
    date = datetime(2026, 1, 1) + timedelta(days=random.randint(0, 300))

    amount_text = random.choice([str(amount), f"₹{amount:,}", f"{amount:,}"])
    if random.random() < 0.04:
        amount_text = "N/A"

    rows.append(
        {
            "Order ID": f"ORD{1000 + i}",
            "Order Date": date.strftime(random.choice(DATE_FORMATS)),
            "Customer Name": random.choice(NAMES),
            "City": random.choice([city, city.lower(), city.upper(), f" {city} ", f"{city} "]),
            "Product": random.choice([product, product.lower(), product.upper()]),
            "Amount (Rs)": amount_text,
            "Qty": random.randint(1, 5),
        }
    )

df = pd.DataFrame(rows)

# Add ~15 exact duplicate rows, then shuffle
df = pd.concat([df, df.sample(15, random_state=1)], ignore_index=True)
df = df.sample(frac=1, random_state=7).reset_index(drop=True)

df.to_csv("messy_sales.csv", index=False)
print(f"Created messy_sales.csv with {len(df)} rows")
