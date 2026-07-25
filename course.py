class Courses:
    def __init__(self, courseCode, courseName, courseCredits, stMarks):
        self.CourseCode = courseCode
        self.CourseName = courseName
        self.CourseCredits = courseCredits
        self.StMarks = stMarks

    def grade_point_value(self):

        m = self.StMarks

        if m >= 85:
            return 4.0
        elif m >= 80:
            return 4.0
        elif m >= 75:
            return 3.7
        elif m >= 70:
            return 3.3
        elif m >= 65:
            return 3.0
        elif m >= 60:
            return 2.7
        elif m >= 55:
            return 2.3
        elif m >= 50:
            return 2.0
        elif m >= 45:
            return 1.7
        elif m >= 40:
            return 1.3
        elif m >= 35:
            return 1.0
        else:
            return 0.0



