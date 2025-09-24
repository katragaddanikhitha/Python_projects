'''
CSCI6651 Introduction to Python Programming
Student Id: 00983208
Student Name: Katragadda Nikhitha
Git Repository: https://github.com/katragaddanikhitha/Python_projects

 '''
# ------ Assignment-4 --------

# Importing the math module to use sqrt function to calculate the distance.

import math

# creating a list to store the names n points

points = []

print("Enter name and points. Enter Q to quit.")

# using a while loop to take the input from the user until the user enters "Q" or "q" to quit.

while True:
    name = input("Enter Point Name > ")
    if name == 'q' or name == 'Q':
        break
    
    #Taking the a, b and c coordinates of the point from the user.
    #checking if the entered coordinates are valid numbers or not.

    a = input("Enter A > ")
    while not a.isnumeric():
        print("Invalid input, enter a number for A.")
        a = input("Enter A > ")
    b = input("Enter B > ")
    while not b.isnumeric():
        print("Invalid input, enter a number for b.")
        b = input("Enter b > ")
        continue
    c = input("Enter c > ")
    while not c.isnumeric():
        print("Invalid input, enter a number for c.")
        c = input("Enter c > ")

    # Converting coordinates to float.

    a = float(a)
    b = float(b)
    c = float(c)

    points.append([name, (a, b, c)])


# list to store the distances between points

result = []

# created nested for loop to calculate the distance between ppoints.
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        p1 = points[i]
        p2 = points[j]
        a1, b1, c1 = p1[1]
        a2, b2, c2 = p2[1]
        distance = math.sqrt((a2-a1)**2 + (b2-b1)**2 + (c2-c1)**2)
        result.append([f"Distance {p1[0]} to {p2[0]}", round(distance, 3)])

# Here I am printing the results

print("\nResults")
for j in result:
    print(f"{j[0]} is {j[1]:.3f}")
