# Personal Monthly Budget Assistant
# Author: Ryan T. Boyd
# Description:
#   Plan categories, log expenses, and print a clean monthly summary
#   showing planned vs actual and helpful warnings for any overages.

from typing import Dict

def get_float(prompt: str, allow_zero: bool = True) -> float:
    """Prompt until a valid float is entered. If allow_zero is False, require > 0."""
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
            if allow_zero:
                if val < 0:
                    print("Please enter a number that is 0 or greater.")
                    continue
            else:
                if val <= 0:
                    print("Please enter a number greater than 0.")
                    continue
            return val
        except ValueError:
            print("That wasn't a number. Try again.")

def get_int(prompt: str, min_value: int = 1) -> int:
    """Prompt until an integer >= min_value is entered."""
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
            if val < min_value:
                print(f"Please enter a whole number >= {min_value}.")
                continue
            return val
        except ValueError:
            print("Please enter a whole number.")

def get_nonempty(prompt: str) -> str:
    """Prompt until a non-empty string is entered."""
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Please enter a non-empty value.")

def summarize(income: float, planned: Dict[str, float], spent: Dict[str, float]) -> None:
    """Compute and print a tidy summary of the month."""
    total_planned = sum(planned.values())
    total_spent = sum(spent.values())
    remaining = income - total_spent

    print("\n=== Monthly Budget Summary ===")
    print(f"Income: ${income:,.2f}")
    print(f"Total Planned: ${total_planned:,.2f}")
    print(f"Total Spent:   ${total_spent:,.2f}")
    print(f"Remaining:     ${remaining:,.2f}\n")

    # Table header
    print(f"{'Category':<18} {'Planned':>12} {'Spent':>12} {'% Plan Used':>14} {'% Income':>12}")
    print("-" * 70)

    any_over = False
    for cat, plan_amt in planned.items():
        actual = spent.get(cat, 0.0)
        pct_plan = (actual / plan_amt * 100.0) if plan_amt > 0 else 0.0
        pct_income = (actual / income * 100.0) if income > 0 else 0.0
        print(f"{cat:<18} ${plan_amt:>11,.2f} ${actual:>11,.2f} {pct_plan:>13.2f}% {pct_income:>11.2f}%")
        if actual > plan_amt:
            over_by = actual - plan_amt
            print(f"  WARNING: {cat} over budget by ${over_by:,.2f}")
            any_over = True

    # Uncategorized bucket if any unknown categories were used
    if spent.get('Uncategorized', 0.0) > 0:
        act = spent['Uncategorized']
        pct_income = (act / income * 100.0) if income > 0 else 0.0
        print(f"{'Uncategorized':<18} {'(no plan)':>12} ${act:>11,.2f} {'n/a':>14} {pct_income:>11.2f}%")

    if any_over:
        print("\nTip: Review over-budget categories and cut discretionary costs next month.")
    else:
        print("\nNice work: All categories are within plan.")

def main() -> None:
    print("Welcome to the Personal Monthly Budget Assistant\n")

    income = get_float("Enter monthly take-home income: ", allow_zero=False)

    planned: Dict[str, float] = {}
    count = get_int("How many budget categories? ", min_value=1)
    for i in range(1, count + 1):
        name = get_nonempty(f"Name for category #{i}: ")
        amount = get_float(f"Planned amount for {name}: ", allow_zero=True)
        # Fold duplicates into the same category
        planned[name] = planned.get(name, 0.0) + amount

    sum_planned = sum(planned.values())
    if sum_planned > income:
        print(f"\nWarning: Your total planned (${sum_planned:,.2f}) exceeds income (${income:,.2f}).")

    # Initialize spent dict and include an Uncategorized bucket
    spent: Dict[str, float] = {k: 0.0 for k in planned.keys()}
    spent["Uncategorized"] = 0.0

    print("\nEnter expenses one by one. Type 'done' as the category to finish.\n")
    while True:
        cat = input("Expense category (or 'done'): ").strip()
        if cat.lower() == "done":
            break
        amount = get_float("Expense amount: ", allow_zero=True)

        if cat in planned:
            spent[cat] = spent.get(cat, 0.0) + amount
        else:
            # Route unknown categories to a catch-all bucket so nothing is lost
            spent["Uncategorized"] += amount

    summarize(income, planned, spent)

if __name__ == "__main__":
    main()
