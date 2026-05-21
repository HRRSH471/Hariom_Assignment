# 16.Finding the Middle Number
# ○ Task: Write a program to determine the middle number among three inputs.
# ○ Input: Prompt the user to enter three numbers.
# ○ Processing: Identify the middle number, which is neither the largest nor the
# smallest.
# ○ Output: Display the middle number.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if (num1 >= num2 and num1 <= num3) or (num1 <= num2 and num1 >= num3):
    print(f"The middle number is: {num1}")
elif (num2 >= num1 and num2 <= num3) or (num2 <= num1 and num2 >= num3):
    print(f"The middle number is: {num2}")
else:
    print(f"The middle number is: {num3}")