# 13. Library Charge Calculation

# Problem Statement:

# Write a javascript program that calculates the library charge based on the number of days a
# book has been borrowed.

# Charge Criteria:
# ● Up to 5 days: Rs. 2 per day
# ● 6 to 10 days: Rs. 3 per day
# ● 11 to 15 days: Rs. 4 per day
# ● More than 15 days: Rs. 5 per day

# Instructions:
# 1. Input: Prompt the user to enter the number of days the book has been borrowed.
# 2. Processing: Calculate the charge based on the given criteria.
# 3. Output: Display the calculated charge.
days_borrowed=int(input("Enter the number of days the book has been borrowed :"))
if days_borrowed <= 5:                                                                              
    charge = days_borrowed * 2  
    print(f"Library charge: Rs. {charge}")
elif days_borrowed >= 6 and days_borrowed <= 10:
    charge = days_borrowed * 3  
    print(f"Library charge: Rs. {charge}")
elif days_borrowed >= 11 and days_borrowed <= 15:
    charge = days_borrowed * 4 
    print(f"Library charge: Rs. {charge}")
elif days_borrowed > 15:    
    charge = days_borrowed * 5 
    print(f"Library charge: Rs. {charge}")      