class Student:
    def __init__(self, stud_id, stud_name, stud_dob):
        self.stud_id = stud_id
        self.stud_name = stud_name
        self.stud_dob = stud_dob

class Course:
    def __init__(self, c_id, c_name):
        self.c_id = c_id
        self.c_name = c_name

class Course_selection: 
    staticmethod                                                                      
    def choose_course(courses):
        print("Select course ID: ")
        for course in courses:
            print(f"ID: {course.c_id}, Name: {course.c_name}")
        chosen_course_id = int(input("Enter the ID of the course you want to choose: "))
        return chosen_course_id

    staticmethod
    def s_mark(students, course):
        marks = []
        for student in students:
            mark = float(input(f"Input mark of student {student.stud_name}: "))
            marks.append((course.c_id, course.c_name, student.stud_id, student.stud_name, mark))
        return marks

def main():
    # Input functions:
    #Input number of students
    stud_number = int(input("Input number of students: "))
    students = []
    #Input student information
    for _ in range(stud_number):
        stud_id = input("Input student ID: ")
        stud_name = input("Input student name: ")
        stud_dob = input("Input student DoB: ")
        student = Student(stud_id, stud_name, stud_dob)
        students.append(student)

    #Input number of courses
    c_number = int(input("Input number of courses: "))
    courses = []
    #Input course information
    for _ in range(c_number):
        c_id = input("Input course ID: ")
        c_name = input("Input course name: ")
        course = Course(c_id, c_name)
        courses.append(course)

    # Listing functions:
    #List students
    print("List of students:")
    for student in students:
        print(f"ID: {student.stud_id}, Name: {student.stud_name}, DoB: {student.stud_dob}")
    #List courses
    print("List of courses:")
    for course in courses:
        print(f"ID: {course.c_id}, Name: {course.c_name}")

    #Select a course, input marks for student in this course
    chosen_course_id = Course_selection.choose_course(courses)
    marks = Course_selection.s_mark(students, courses[chosen_course_id-1])

    #Show student marks for a given course
    print("Student marks in the chosen course is:")
    print("(Course ID, Course name, Student ID, Student name, Mark)")
    for mark in marks:
        print(mark)

main()