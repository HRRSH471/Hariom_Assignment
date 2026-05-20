# 5. Task: Salary Calculation
# ● Objective: You have to calculate an employee's salary by computing the gross
# salary tax and net salary based on the given parameters.
# ● Hints:
# ○ Base Salary = ₹50000
# ○ Bonus = ₹5000
# ○ Tax Rate = 10%
# ○ Other Charges = ₹2000
# Display the Gross Salary Tax and Net Salary.

Base_salary= 50000
Bonus=5000
Tax_Rate=10
other_charge=2000
Gross_salary=Base_salary+Bonus
Tax=10/100*Gross_salary
net_salary=Gross_salary-Tax-other_charge
print(f"Your Gross Salary ",Gross_salary)
print(f"Your Net Salary afte Tax and other charges" ,net_salary)
print(f"Your Tax ",Tax)