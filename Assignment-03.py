
'''
CSCI6651 Introduction to Python Programming
Student Id: 00983208
Student Name: Katragadda Nikhitha
Git Repository: https://github.com/katragaddanikhitha/Python_projects
-Create a Python script that will capture capture grades for a group of Students.
-Your script must collect the grades as alpha characters F to A+ for a Student
-It must then compute a grade point average of 0 to 5.0 for each Student.

 '''
# Grade to GPA mapping(0.0-5.0 scale)
gmap = {
    "A+": 5.0, "A": 4.7, "A-": 4.3,
    "B+": 4.0, "B": 3.7, "B-": 3.3,
    "C+": 3.0, "C": 2.7, "C-": 2.3,
    "D+": 2.0, "D": 1.7, "D-": 1.0,
    "F": 0.0
}

all_stdgrades = []   # created a list to store all student grades
all_stdgpa = []      # created a list to store all student gpa

n = 1
#Created an infinite loop to take input from user until user enters 'Q' to quit
while True:
    data = input(f"Enter grades for Student {n} (F-A+) or Q to quit > ")
# If user enters 'Q' the loop will break and program will end    
    if data.upper() == "Q":
        break
# Splitting the input string by comma and removing any extra spaces
    grades = [x.strip().upper() for x in data.split(",")]
# Appending the grades to the all_stdgrades list   
    all_stdgrades.append(grades)
#converting grades to gpa if it exists in the gmap dictionary
    points = [gmap[g] for g in grades if g in gmap]
# Calculating the GPA by taking the average of the points and rounding it to 2 decimal places
    gpa = round(sum(points) / len(points), 2)
# Appending the gpa to the all_stdgpa list
    all_stdgpa.append(gpa)
# Printing the GPA for each student
    print(f"Student #{n} GPA: {gpa}")
# Incrementing the student number
    n += 1
# Printing all the student grades and gpas
print("\nGrades:", all_grades)
print("GPAs:", all_gpa)


