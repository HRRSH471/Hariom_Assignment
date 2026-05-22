# 18.Authentication System
# ○ Task: Write a program to authenticate a user by validating their username and
# password.
# ○ Predefined Credentials:
# ■ Username: user1
# ■ Password: pass@123
# ○ Input: Prompt the user to input their username and password.
# ○ Output:
# ■ If the credentials match, display "Authentication successful."
# ■ If they do not match, display "Authentication failed."
username = "user"
password ="pass@123"
usernam = input("Enter your User Name :")
psd = input("Enter your User Password :")
if username==usernam and psd==password:
    print(usernam,"Your Are Authorzied User")
else:
    print(username, "Your Are Not Authorized User")
    