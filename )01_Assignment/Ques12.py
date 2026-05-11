# Calculate Simple Interest
principal=float(input("Enter the principal amount "))
rate=float(input("Enter Rate of Interest "))
time=float(input("Enter Year "))
# Formula: SI = (P * R * T) / 100
simple_interest = (principal * rate * time) / 100

print(f"Simple Interest = {simple_interest}")
