# 17.Find the greatest number.
# ○ Task: Write a program to find greatest number from three number
# ○ Input: Prompt the user to enter three numbers.
# ○ Output: Display the greatest number.
num1=int(input("Enter the First Number : "))
num2=int(input("Enter the Second Number : "))
num3=int(input("Enter the Third Number : "))
if num1 >= num2 and num1 >= num3:
    print(f"Greatest Number is : ",num1)
elif num2 >=num1 and num2 >= num3:
    print(f"Greatest Number is : " , num2)
elif num3 >= num1 and num3 >= num2:
    print(f"Greatest Number is : ",num3)
