name=input("enter the name:")
monthly_income=float(input("enter the monthly income:"))
rent=float(input("enter the rent:"))
food_expenses=float(input("enter the food expenses:"))
travel_expenses=float(input("enter the travel expenses:"))
entertainment_expenses=float(input("enter the entertainment expenses:"))
other_expenses=float(input("enter the other expenses:"))
total_expenses=rent+food_expenses+travel_expenses+entertainment_expenses+other_expenses
reamaining_money=monthly_income-total_expenses
savings_percentage=(reamaining_money/monthly_income)*100
# Display the result
print("\n=====MONTHLY EXPENSE REPORT=====")
print(f"Name:{name}")
print(f"Monthly income:₹ {monthly_income:.2f}")
print(f"Food expenses:₹{food_expenses:.2f}")
print(f"rent:₹{rent:.2f}")
print(f"Entertainment expenses:₹{entertainment_expenses:.2f}")
print(f"Other expenses:₹{other_expenses:.2f}")
print(f"Total expenses:₹{total_expenses:.2f}")
print(f"remaining money:₹{reamaining_money:.2f}")
print(f"Savings percentage:₹{savings_percentage:.2f}")