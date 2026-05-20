# 4. Task: Calculate the Area of a Circle
# ● Objective: Write a program to calculate the area of a circle.
# ● Hints:
# ○ Ask the user to input the radius of the circle.
# ○ Calculate the area of the circle using the formula: Area = π *
# radius^2.
# ○ Display the calculated area
radius=int(input("Enter the radius of circle "))
if radius>=0:
    area_of_circle=22/7*radius**2
print(f"Are of Circler with Radius {radius}, is {area_of_circle} ")