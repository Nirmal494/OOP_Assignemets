class Student:
    def __init__(self, stId, stName, stAge, stDegreeProgram ):
        self.StId = stId
        self.StName = stName
        self.StAge = stAge
        self.StDegreeProgram = stDegreeProgram
        self.StRgCourses = []

    def student_course_registration(self, *courses):

        for course in courses:
            self.StRgCourses.append(course)