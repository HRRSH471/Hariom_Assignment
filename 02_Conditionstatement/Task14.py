# 14. Arranging Three Numbers in Descending Order

# Task:
# Write a javascript program to arrange three numbers in descending order.

# Input:
# Prompt the user to enter three numbers.

# Processing:
# Sort the numbers in descending order.
# Example:
# ● Enter first number: 3
# ● Enter second number: 1
# ● Enter third number: 2
# Output:
# ● Numbers in Descending Order: 3, 2, 1  
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print(f"Numbers in Descending Order: {num1}, {num2}, {num3}")
    else:
        print(f"Numbers in Descending Order: {num1}, {num3}, {num2}")
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print(f"Numbers in Descending Order: {num2}, {num1}, {num3}")
    else:
        print(f"Numbers in Descending Order: {num2}, {num3}, {num1}")
else:
    if num1 >= num2:
        print(f"Numbers in Descending Order: {num3}, {num1}, {num2}")
    else:
        print(f"Numbers in Descending Order: {num3}, {num2}, {num1}")
