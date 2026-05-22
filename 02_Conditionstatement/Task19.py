# 19.Calculate Class Attendance Percentage
# ○ Task: Write a program to calculate the percentage of classes attended by a
# student and determine their eligibility to sit in the exam.
# ○ Conditions:
# ■ Attendance percentage < 75%: Not eligible to sit in the exam.
# ■ Attendance percentage ≥ 75%: Eligible to sit in the exam.
# ○ Output: Display the attendance percentage and eligibility status.

# 19.Calculate Class Attendance Percentage
Name=input("Enter Your Name : ")
clas_addenence=int(input("Enter the No of Days You Attend the Class in 365 Days: "))
attendence_percentage=clas_addenence/365*100

if attendence_percentage >=75:
    print(Name,"You are eligible for exam because your attendence percentage is ",attendence_percentage)
else:
    print(Name,"You are not eligible for exam because your attendence percentage is " ,attendence_percentage)
