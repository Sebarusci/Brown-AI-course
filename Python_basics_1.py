# Object Oriented Programming & Classes
class Student:
    def __init__(self, name, age, grade): # --> Class constructor
        self.name= name
        self.age = age             #-----> Instance variables
        self.grade = grade

    def student_info(self):             # -----> Internal funtion
        print("Student name: " + self.name)
        print("Student age: " + str(self.age))
        print("Student grade: " + self.grade)

#student1 = Student("Sebastiano", 16, "12th")
#student1.student_info()

print("===========")

class Course:
    def __init__(self, name, GPA, teacher):
        self.name = name
        self.GPA = GPA
        self.teacher = teacher

    def course_info(self):
        print("The course name is: " + self.name)
        print("The course GPA is: " + str(self.GPA))
        print("The course instructor is: " + self.teacher)

#course1 = Course("Artificial Intelligence", "N/A", "Benedict Quartey")
#course1.course_info()