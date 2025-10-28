# Personal Monthly Budget Assistant

Console app to plan monthly categories, log expenses, and print a clean summary of planned vs actual spending.

## How it works
- You enter take-home income.
- Add your budget categories and planned amounts.
- Enter expenses one-by-one (any unknown category goes to **Uncategorized**).
- Get a summary with totals, percents, and warnings for any over-budget categories.

## Run locally
```bash
python3 main.py
```

## Run on Replit
1. Create a new **Python** Repl.
2. Upload all files from this folder or drag-drop the zip.
3. Make sure the project is public.
4. Press **Run**.

## Sample session
```
Enter monthly take-home income: 3000
How many budget categories? 4
Name for category #1: Rent
Planned amount for Rent: 1200
Name for category #2: Food
Planned amount for Food: 400
Name for category #3: Transportation
Planned amount for Transportation: 200
Name for category #4: Savings
Planned amount for Savings: 600

Enter expenses one by one. Type 'done' as the category to finish.

Expense category (or 'done'): Food
Expense amount: 55.2
Expense category (or 'done'): Transportation
Expense amount: 45
Expense category (or 'done'): Food
Expense amount: 110.33
Expense category (or 'done'): Rent
Expense amount: 1200
Expense category (or 'done'): Savings
Expense amount: 600
Expense category (or 'done'): done
```
