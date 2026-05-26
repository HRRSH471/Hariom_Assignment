# 4.Write a Python program to check if a number provided by the user is prime or not.
num=int(input("enter your number: "))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num, "is not Prime Number")
            break
            
        else:
            print(num,"is prime number")
            break
else:
    print(num, "Number is less than one")            




            
        
