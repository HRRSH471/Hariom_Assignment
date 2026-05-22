# 20.Library Charge Calculation
# ○ Task: Write a program to calculate the library charges based on the number of
# days a book has been borrowed.
# ○ Charge Criteria:
# ■ Up to 5 days: ₹2/day.
# ■ 6 to 10 days: ₹3/day.
# ■ 11 to 15 days: ₹4/day.
# ■ More than 15 days: ₹5/day.
# ○ Output: Display the total charges
Name=input("Enter Your Name : ")
day=int(input("Please enter the days for your borrow the book : "))
if day<=5:
    library_charge=day*2
    print(Name,"Your Total Library Charge is : ",library_charge)
elif day>=6 and day<=10:
    library_charge=day*3
    print(Name,"Your Total Library Charge is : ",library_charge)
elif day>=11 and day<=15:    
    library_charge=day*4
    print(Name,"Your Total Library Charge is : ",library_charge)
elif day>15:
    library_charge=day*5
    print(Name,"Your Total Library Charge is : ",library_charge)





 
