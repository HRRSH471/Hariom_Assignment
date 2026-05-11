# Add 20 % discount to a price
print("Enter the price of the product:")
price=int(input()) # This take price from user
print("Enter the discount %..")
discount=int(input()) # This take discount from user
final_price=price-price*discount/100
print(f"Final Price After Discount={final_price}")