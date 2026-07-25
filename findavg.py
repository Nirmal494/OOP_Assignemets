import course
from student import Student
from course import Courses

course_01 = Courses("C12063", "Data Structures and Algorithms", 3,75 )
course_02 = Courses("C12053", "Probability and Statistics", 3,80 )
course_03 = Courses("C12044", "System Analysis and Design",2 , 65)
course_04 = Courses("C12023", "Operating Systems",4 , 55)
course_05 = Courses("C12070", "Web Development", 3, 76)

student_01 = Student("S1001", "M.S.K.Pereira", 21, "Software Engineering")

student_01.student_course_registration(course_01, course_02, course_03, course_04, course_05)

def cal_average(student):
    total =0
    for m in student_01.StRgCourses:
        total = total + m.StMarks

    avg = total / len(student_01.StRgCourses)

    return avg

average = cal_average(student_01)
print(average)

def cal_GPA(student):

    total_quality_points = 0
    total_credits = 0
    for c in student_01.StRgCourses:
        grade_points = c.grade_point_value()
        quality_points = grade_points * c.CourseCredits

        total_quality_points = total_quality_points + quality_points
        total_credits = total_credits + c.CourseCredits

    gpa = total_quality_points / total_credits
    return gpa

gpa1 = cal_GPA(student_01)
print(f"Student ID: {student_01.StId}, Student Name: {student_01.StName}, GPA = {gpa1}")





