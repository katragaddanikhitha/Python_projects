
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
    if data == "Q":
        break
# Splitting the input string by comma and removing any extra spaces
    grades = data.split(",")
    usr_inp = True

    for j in grades:
        if j not in gmap:
            print("Invalid grade entered. Please enter grades between F and A+.")
            usr_inp = False
            break
    
    if not usr_inp:
        continue
    # Appending the grades to the all_stdgrades list
    all_stdgrades.append(grades)
    total = 0
    
    for k in grades:
            total = total + gmap[k]
    gpa = total / len(grades)
    # Appending the gpa to the all_stdgpa list
    all_stdgpa.append(round(gpa,2))
    n += 1
# Printing all the student grades and gpas
for i in range(len(all_stdgpa)):
    print(f"Student #{i + 1} GPA: {all_stdgpa[i]}")

print(f"Total number of students: {len(all_stdgrades)}")
print(f"Average GPA: {round(sum(all_stdgpa) / len(all_stdgpa), 2)}")

