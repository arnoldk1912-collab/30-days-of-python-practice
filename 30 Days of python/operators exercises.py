age = 22
height = 6.1
comp = 1 + 2j

# Base and hight of the traiangle 

base = float(input("Enter your base:"))
height = float(input("Enter your hight:"))
area_of_the_traiangle = 0.5 * base * height
print("Area of the traiangle is", area_of_the_traiangle)

# perimeter of the triangle

side_a = float(input("Enter your side a:"))
side_b = float(input("Enter your side b:"))
side_c = float(input("Enter your side c:"))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is", perimeter)

# Length and width of the rectangle

length = float(input("Enter your length:"))
width = float(input("Enter your width:"))
area = length * width
perimeter = 2 * (length + width)
print("The area of a rectangle", area)
print("the perimeter of a recatangle", perimeter)

# Radius and area of circle

import math

radius = float(input("What is your radius:"))
area = math.pi * radius * radius
circumference = 2 * math.pi * radius
print("Area of a circle", area)
print("Circumference of a circle", circumference)

# Calculate the slope

slope_8 = 2
x_intercept = 1
y_intercept = -2
print("slope", slope_8)
print("X intercept", x_intercept)
print("Y intercept", y_intercept)

point_1 = (2, 2)
point_2 = (6, 10)

x1 = point_1[0]
y1 = point_1[1]
x2 = point_2[0]
y2 = point_2[1]

slope_9 = (y2 - y1) / (x2 - x1)
distance = math.sqrt ((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("Slope", slope_9)
print("Distance", distance)

if slope_8 == slope_9:
    print("Both are equal")
else:
    print("which one is bigger")
    
x = -3
y = x ** 2 + 6*x + 9
print("X =", x)
print("Y =", y)


len_python = len("python")
len_dragon = len("dragon")

print(len_python != len_dragon)

print("on" in "python" and "on" in "dragon")