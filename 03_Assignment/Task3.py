#3.Write a Python program to generate a table of a number provided by the user.
num=int(input("Enter the Number To Generate Table : "))
print("Table of",num,"is given below")
for i in range(1,11):
    
    print(i*num)
