# Sales Data Cleaning

## Problem
A sales file with 315 rows had many problems. Wrong text, mixed date formats, duplicate rows and missing values. It could not be used for a report.

## What I fixed
1. Cleaned column names
2. Removed 15 duplicate rows (315 → 300)
3. Made city and product names the same (5 cities, 5 products)
4. Converted amounts like `₹1,200` into numbers
5. Read 3 different date formats correctly
6. Filled 72 missing customer names with "Unknown"
7. Kept 9 rows with invalid amounts in a separate sheet. I did not delete them.

## Result
`sales_report.xlsx` has 5 sheets:
- `clean_data` (291 rows)
- `bad_rows` (9 rows)
- `by_city`
- `monthly`
- `top_products`

## Tools
Python, Pandas, openpyxl, Jupyter Notebook

## Note
The data is sample data made by `make_messy_data.py` for practice. It is not from a real client.
