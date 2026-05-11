# Percentage Increase or Decrease

initial_value = 200
final_value = 250

# Calculate percentage change
percentage_change = ((final_value - initial_value) / initial_value) * 100

# Check increase or decrease
if percentage_change > 0:
    print(f"Percentage Increase = {percentage_change}%")
elif percentage_change < 0:
    print(f"Percentage Decrease = {abs(percentage_change)}%")
else:
    print("No Change")
    