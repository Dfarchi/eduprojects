# Write a program that receives the width and the height of a rectangle
# and prints the area and the perimeter of the rectangle.

width = int(input("Insert rectangle width: "))
height = int(input("Insert rectangle height: "))
area = width * height
perimeter = 2 * (width + height)
print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")