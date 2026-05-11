# Calculate Compund Interest
principal=float(input("Enter the principal amount "))
rate=float(input("Enter Rate of Interest "))
time=float(input("Enter Year "))
# Calculate Amount
amount = principal * (1 + rate/100) ** time
# Calculate Compound Interest
compound_interest = amount - principal
print(f"Total Amount = {amount}")
print(f"Compound Interest = {compound_interest}")