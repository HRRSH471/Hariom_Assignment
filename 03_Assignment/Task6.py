#Write a Python program to generate the Fibonacci sequence up to a specified
# number of terms.


num = int(input("Enter how many Fibonacci numbers you want: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(num):

    print(a)

    c = a + b
    a = b
    b = c