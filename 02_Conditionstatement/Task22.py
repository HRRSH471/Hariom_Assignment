# 22. Menu-Driven Login System
# 1. Create the Menu:
# ○ Display a menu with three choices for the user:
# ■ Login with Phone
# ■ Login with Email
# ■ Exit the system
# 2. Predefined Credentials:
# ○ Phone number: "1234567890"
# ○ OTP: "1234"
# ○ Email: "user@example.com"
# ○ Password: "password123”
# 3. Login Functionality:
# ○ Option 1 (Login with Phone):
# ■ Prompt the user to enter their phone number and OTP.
# ■ Compare the input with a predefined phone number and OTP.
# ■ Display success if both match or an error message if they don’t.
# ○ Option 2 (Login with Email):
# ■ Prompt the user to enter their email and password.
# ■ Compare the input with predefined email and password.
# ■ Display success if both match or an error message if they don’t.
# ○ Option 3 (Exit):
# ■ Display an exit message and terminate the program.
# ○ Invalid Input:
# ■ Handle invalid user choices and ask the user to select a valid option.
# Output:
# 1. If the user enters a valid phone number and OTP, display: "Login successful
# with phone!"
# 2. If the user enters valid email and password, display: "Login successful
# with email!"
# 3. If the user selects the exit option, display: "Exiting the program. Have a
# nice day!"
# 4. If the user enters invalid credentials or an invalid choice, display appropriate error
# messages.
phone_number="123456789"
otp="1234"
Email="user@example.com"
Password="password123"
exit="Exit"
usenumber=int(input("Enter Your Phone Number : "))
userotp=int(input("Enter Your OTP : "))
useremail=input("Enter Your Email ID : ")
userpswd=input("Enter Your Password : ")
userexit=input("Enter Exit to Terminate the Program")
if phone_number==usenumber and otp==userotp:
    print("You are Login Successfuly with Phone")
elif Email==useremail and Password==userpswd:
    print("You are Login Successfuly with Email")
elif exit==userexit:
    print("You are Terminate from program")
else:
    print("Your Enter the the Invalid Credential")