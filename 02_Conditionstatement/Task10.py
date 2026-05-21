# 10.Task : Student Grading System
# Create a javascript program to calculate a student's grade based on their marks.
# Task:
# 1. Input: Prompt the user to enter their marks.
# 2. Criteria:
# ○ Grade A: 90–100
# ○ Grade B: 80–89
# ○ Grade C: 70–79
# ○ Grade D: 60–69
# ○ Grade E: 50–59
# ○ Grade F: 0–49
# ○ Invalid marks: Outside the range 0–100.
# 3. Output: Display the grade or an error message for invalid marks.
# Example Outputs:
# ● Marks: 85 → Grade: B
# ● Marks: 45 → Grade: F
# ● Marks: 105 → Invalid marks
marks=int(input("Enter your marks :"))
if marks >= 90 and marks <=100:
    print("Your Grade is A")
elif marks >= 80 and marks <=89:
    print("Your Grade is B")  
elif marks >= 70 and marks <=79:
    print("Your Grade is C") 
elif marks >=60 and marks <= 69:
    print("Your Grade is D")   
elif marks >=50 and marks <=59:
    print("Your Grade is E")
elif marks >=0 and marks <=49:
    print("Your Grade is F") 
else:
    print("Invalid Marks Enter")        