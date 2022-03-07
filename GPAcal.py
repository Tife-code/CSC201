'''
    This program recieves the courses, course units, scores and calculates the GPA of any given number of students
    It works without having any function, kindly check it out
'''
import sys
Grading = {"A": 70-100, "B": 60-69, "C": 50-59, "D": 45-49, "E": 40-44, "F": 0-39}
Grade= {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0}

#creating lists to store courses, course units and scores of student
Courses = []
Units =[]
Scores=[]
try:
    numberOfStudents = int(input("Hello, how many students GPA do you want to calculate: "))
except ValueError:
    print("Value must be a number!")
    numberOfStudents = int(input("Hello, how many students GPA do you want to calculate: "))

num=0
while num < numberOfStudents:
    name = input("Name of student: ")
    okay =0 
    try:
        numberOfCourses= int(input("How many courses did you register for(between 5 and 10): "))
    except ValueError:
        print("Please, Enter a number between 5 and 10")
        numberOfCourses= int(input("How many courses did you register for(between 5 and 10): "))
    if numberOfCourses == 0 or numberOfCourses<5: 
        print('You have to register for 5 or more courses')
        continue
    elif numberOfCourses > 10:
        print('You can\'t register for more than 10 courses')
        continue
    else:
        while okay < numberOfCourses:
            try:
                courseCode = input("Enter your course code and the unit separated by column (Course code: unit)==> ")
                Courses.append(courseCode.split(":")[0].upper())
                Units.append(int(courseCode.split(":")[1]))
            except :
                print("Oops!", sys.exc_info()[2], "occurred.")
                print("Check the entry format and try again!")
                courseCode = input("Enter your course code and the unit separated by column (Course code: unit)==> ")
                Courses.append(courseCode.split(":")[0].upper())
                Units.append(int(courseCode.split(":")[1]))
            try:
                score = int(input("Enter your score: "))
            except ValueError:
                print("Score must be a number!")
                score = int(input("Enter your score: "))
            Scores.append(score)
            okay +=1

        TotalWorkload=sum(Units)
        if TotalWorkload ==0 or TotalWorkload < 18 or TotalWorkload >24:
            print("Your total workload must be MINIMUM of 18 and MAXIMUM of 24")
        
        creditPoints = []
        Grades= []
        for x in range(len(Scores)):
            if Scores[x] == 0 or Scores[x] <=39:
                creditPoint = Units[x]*0
                creditPoints.append(creditPoint)
                Grades.append("F")

            elif Scores[x] == 40 or Scores[x]<= 44:
                creditPoint= Units[x]*1
                creditPoints.append(creditPoint)
                Grades.append("E")

            elif Scores[x] == 45 or Scores[x]<= 49:
                creditPoint= Units[x]*2
                creditPoints.append(creditPoint)
                Grades.append("D")

            elif Scores[x] == 50 or Scores[x]<= 59:
                creditPoint= Units[x]*3
                creditPoints.append(creditPoint)
                Grades.append("C")

            elif Scores[x] == 60 or Scores[x]<= 69:
                creditPoint= Units[x]*4
                creditPoints.append(creditPoint)
                Grades.append("B")
            
            elif Scores[x] == 70 or Scores[x] <= 100:
                creditPoint= Units[x]*5
                creditPoints.append(creditPoint)
                Grades.append("A")

        
    GPA =  sum(creditPoints)/TotalWorkload    
    print(f"{name.upper()} is offering {Courses} \nScored the following {Scores} \nGrades are {Grades} respectively")
    print("===============================================================")
    print(f"Total Credit Point(TCP) : {sum(creditPoints)} \nTotal Workload(TWL) : {TotalWorkload} \nGPA : {round(GPA,3)} \n")  
    
    Courses.clear() 
    Units.clear()
    Scores.clear()
    Grades.clear()
    num+=1
