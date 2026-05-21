# 11.Task : Authentication System.

# Write a javascript program that authenticates a user by checking their username and
# password. The program should compare the entered credentials with predefined valid
# credentials.
# ● Predefined valid usernames and corresponding passwords
# username1 = "user1"
# username1_password1 = "pass@123"
# Instructions:
# 1. Input:
# ○ Prompt the user to input their username and password.
# 2. Processing:
# ○ Check if the username and password match
# 3. Output:
# ○ If both the username and password match the predefined valid credentials
# display "Authentication successful."
# ○ If either the username or the password does not match displayus
# "Authentication failed."
username1="user1"
username1_password1="pass@123"
username2=input(" Enter your user name")
username2_password2=input("Enter your password")
if username1 == username2 and username1_password1 == username2_password2:
   print("you are valid user")
else:
   print("you are not a valid user")