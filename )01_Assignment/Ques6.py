# Increase Shopping Cart items
cart_items = 5

print(f"Current Available Items In Cart = {cart_items}")
print("Enter item to add in cart:")

add_item = int(input())   # take input and convert to integer

final_cart_item = cart_items + add_item

print(f"Final Available Items In Cart = {final_cart_item}")