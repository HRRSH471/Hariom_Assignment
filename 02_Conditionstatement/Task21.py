# 21.UPSC Selection Process

# ○ Task: Simulate the UPSC selection process with the following steps:
# 1. Eligibility Check
# ■ Criteria:
# ■ Age: 21–32 years.
# ■ Graduate status: Must be a graduate.
# ■ Nationality: Must be "Indian".
# ■ Output:
# ■ If eligible, proceed to Prelims.
# ■ If ineligible, display the reason for ineligibility.
# 2. Prelims Exam
# ■ Processing: Check if the candidate’s score ≥ cut-off.
# ■ Output:
# ■ If passed, proceed to Mains.
# ■ If failed, display "You failed the Prelims."
# 3. Mains Exam
# ■ Processing: Check if the candidate’s score ≥ cut-off.
# ■ Output:
# ■ If passed, proceed to Interview.
# ■ If failed, display "You failed the Mains."
# 4. Interview
# ■ Processing: Check if the candidate’s score ≥ cut-off.
# ■ Output:
# ■ If passed, display "Congratulations! You have cleared the
# UPSC."
# ■ If failed, display "You failed the Interview."
# ○ Final Output: Use nested conditional statements to simulate the entire process.
Name=input("Enter Your Name")
Age=int(input("Enter Your Age : "))
Graduation_status=(input("Are you graduate yes/no"))
Nationality=input("Enter your nationality")
if Age>=21 and Age<=32 and Graduation_status=="yes" and Nationality=="indian":
    print("You are eligible for prelims")
    prelims_marks=int(input("Enter your prelims marks out of 200: "))
    if prelims_marks>=200:
        print("You passed the prelims and eligible for mains : ")
        main_marks=int(input("Enter your main marks out of 1750: "))
        if main_marks>=1750:
            print("You Passed in Main Exam and Your Are Eligible For Interview : ")
            interview_marks=int(input("Enter Your interview Marks Out of 275"  ))
            if interview_marks>=275:
                print("Congratulation", "You Clear The UPSC")
            else:
                print("You Failed in Interview")
        else:
            print("You Faild In Main Exam Not Eligible For Interview")    
    else:
        print("Your failed in prelims")
else:
    print("You are not eligible for UPSC")        


            






else:
    print("You are not eligible for prelims")


