#prompt user to input their monthly income and total monthly expenses
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your monthly expenses:"))

#calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

#calculate projected savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#print results
print("Your monthly savings are", "$", monthly_savings)
print("Projected savings after one year, with interest", "is","$", projected_savings)
