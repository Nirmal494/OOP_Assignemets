from abc import ABC, abstractclassmethod
class Student(ABC):
    def __init__(self, stId, stName, stAge, stDegreeProgram ):
        self.StId = stId
        self.StName = stName
        self.StAge = stAge
        self.StDegreeProgram = stDegreeProgram
        self.StRgCourses = []

    @abstractclassmethod
    def st_registration(self):
        pass

    @abstractclassmethod
    def st_details(self):
        pass

    def student_course_registration(self, *courses):

        for course in courses:
            self.StRgCourses.append(course)

class DegreeStudent(Student):
    def __init__(self, stId, stName, stAge, stProgram, degreeFees):
        super().__init__(stId, stName, stAge, stProgram)
        self.degreeFees = degreeFees

    def student_registration(self):
        self.StName = input("Student Name:")
        self.StId = int(input("Enter Student ID:"))
        self.StAge = int(input("Age:"))
        self.StProgram = input("What is the program student registered:")

    def st_allDetails(self):
        print("----Degree programs student details----")
        print(f"Student ID: {self.StId}")
        print(f"Student Name: {self.StName}")
        print(f"Student Age: {self.StAge}")
        print(f"Student Degree program: {self.StProgram}")

class CourseStudent(Student):
    def __init__(self, stId, stName, stAge, stProgram):
        super().__init__(stId, stName, stAge, stProgram)

    def student_registration(self):
            self.StName = input("Student Name:")
            self.StId = int(input("Enter Student ID:"))
            self.StAge = int(input("Age:"))
            self.StProgram = input("What is the program student registered:")
    
    def st_allDetails(self):
            print("----Course programs student details----")
            print(f"Student ID: {self.StId}")
            print(f"Student Name: {self.StName}")
            print(f"Student Age: {self.StAge}")
            print(f"Student Course  program: {self.StProgram}")
