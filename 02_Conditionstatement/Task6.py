# 6. Task: Bank Loan Approval System
# ● Objective: You have to create a javascript script that checks whether an user is
# eligible for a bank loan based on various criteria.
# ● Hints:
# ○ The applicant's age must be between 18 and 60 years.
# ○ The applicant's monthly income must be greater than or equal to ₹25000.
# ○ The applicant's credit score must be greater than or equal to 700.
# ○ The applicant must not have any outstanding debts greater than ₹10000
# 1. Output:
# ○ Display "Loan Approved" if the applicant meets all the conditions.
# ○ Otherwise display "Loan Rejected".
age=input("Enter your age between 18 to 60: ")
monthly_income=int(input("Enter your month income:  "))
credit_score= int(input("Enter your credit Score: "))

outstanding_debt=int(input("Enter the outstanding  debt amount"))
if monthly_income  >=25000 and credit_score>=700 and outstanding_debt <= 10000:
    # outstanding_debt=int(input("Enter the outstanding  debt amount"))
# elif outstanding_debt <= 10000:
    print("Your application is approved")   
else:             
    print ("Your loan application rejected")
   
     

    


