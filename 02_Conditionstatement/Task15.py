# 15. Tax Calculation for Car Purchase
# Write a program to calculate the tax on a car purchase based on the car brand and its price.
# 1. Mahindra: 5% tax for prices between 7L (7 lakh) and 10L.
# 2. Audi: 10% tax for prices between 10L and 15L.
# 3. Jaguar: 25% tax for prices between 15L and 20L.
# 4. Mercedes: 30% tax for prices between 20L and 25L.
# 5. Input: The car brand and price.
# 6. Output: The calculated tax on the purchase.
car_brand=input("Enter the car brand :")
car_price=float(input("Enter the car price :")) 
if car_brand == "Mahindra" and car_price >= 700000 and car_price <= 1000000:
    tax = car_price * 0.05
    print(f"The tax on the purchase is: Rs. {tax:.2f}")
elif car_brand == "Audi" and car_price >= 1000000 and car_price <= 1500000:
    tax = car_price * 0.10
    print(f"The tax on the purchase is: Rs. {tax:.2f}")
elif car_brand == "Jaguar" and car_price >= 1500000 and car_price <= 2000000:
    tax = car_price * 0.25
    print(f"The tax on the purchase is: Rs. {tax:.2f}")
elif car_brand == "Mercedes" and car_price >= 2000000 and car_price <= 2500000:
    tax = car_price * 0.30
    print(f"The tax on the purchase is: Rs. {tax:.2f}")
else:
    print("Invalid car brand or price.")
