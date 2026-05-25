# Write a Python program to generate all multiples of 12.
for i in range(1,12,1):
    if 12%i==0:
        print(i, end=" ")
