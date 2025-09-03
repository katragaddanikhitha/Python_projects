''' 
Illustrate in line and multiline comments.
CSCI6651 Introduction to Python Programming
Student Id: 00983208
Student Name: Katragadda Nikhitha
Git Repository: https://github.com/katragaddanikhitha/Python_projects

 '''


# Assign x='Hello World' 

x = 'Hello World'
# print(x) within your script.
print(x)
# Identify the variable type of x and print type of variable
print(type(x))

# Using string concatenation to modify the "Hello World', by implementing y=x+'1'.
y = x + '1'
# Existing Object x modified to become 'Hello Wolrd1'
print(y)

'''
The above example explains few charateristics of strings in python

1. strings are characters, declared in single(') or double(" ") quotes.
2. Value of a string variable remains unchanged, even though we create a new variable with help of it 
   unless we assign a new value to it. 
3. Type of a string variable in python is mentioned as <class 'str'>.

'''

print(id(x))
print(id(y))

'''

For the statement "does x reference the same Object before and after",
The memory IDs of x and y differ because, while y was initialized using x, 
Python created a new object for y. Hence, the original object referenced by x remains unaffected.”

'''