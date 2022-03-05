#Given the assignment to write the program to calcualte the gpa of 3 differnt students using the following grades;
#70-100 as A, 50-69 as B and 0-49 as E with a minimum of 5 courses for each student.
#this works for just a fixed given set of data. no input!

Grading = {"70-100": "A", "50-69": "B", "0-49": "E"}
Grade= {"A": 5, "B": 4, "E": 1}
Courses = {"MEE": 5, "CSC": 3, "MTH": 5, "STT": 4, "CPE":4}
Units =[]
for unit in Courses.values():
    Units.append(unit)

TotalWorkload = sum(Units)

studentOne = [23,33,77,57,60]
studentTwo = [45,78,32,80,50]
studentThree = [34,75,21,43,54]

students =[studentOne,studentTwo, studentThree]

y=1
while y < 4:
    x=0
    creditPoints = []
    while x <5:
        if students[y-1][x] == 0 or students[y-1][x] <=49:
            creditPoint= Units[x]*1
            creditPoints.append(creditPoint)

        elif students[y-1][x] == 50 or students[y-1][x]<= 69:
            creditPoint= Units[x]*4
            creditPoints.append(creditPoint)

        elif students[y-1][x] == 70 or students[y-1][x] <= 100:
            creditPoint= Units[x]*5
            creditPoints.append(creditPoint)

        x = x+1
    print(f" Student{y} \nTotal Credit Point(TCP) : {sum(creditPoints)} \nTotal Workload(TWL) : {TotalWorkload} \nGPA : {sum(creditPoints)/TotalWorkload} \n")
    y = y+1
