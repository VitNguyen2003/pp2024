import math
import numpy as np
import curses
class Student:
    def __init__(self, stud_id, stud_name, stud_dob):
        self.stud_id = stud_id
        self.stud_name = stud_name
        self.stud_dob = stud_dob

class Course:
    def __init__(self, c_id, c_name):
        self.c_id = c_id
        self.c_name = c_name

class Course_sel: 
    @staticmethod                                                                      
    def choose_course(courses):
        print("Select course ID: ")
        for course in courses:
            print(f"ID: {course.c_id}, Name: {course.c_name}")
        chosen_course_id = int(input("Enter the ID of the course you want to choose: "))
        return chosen_course_id

    @staticmethod
    def stud_mark(students, course):
        marks = []
        for student in students:
            mark = float(input(f"Input mark of student {student.stud_name}: "))
            #Use math module to round-down student scores to 1-digit decimal upon input, floor()
            rounded_mark = math.floor(mark * 10)/10
            marks.append((course.c_id, course.c_name, student.stud_id, student.stud_name, rounded_mark))
        return marks

#Use numpy module and its array to
#Add function to calculate average GPA for a given student
def calculate_average_gpa(marks):
    arr = np.array(marks)
    gpa = np.mean(arr)
    return gpa

#Weighted sum of credits and marks
def weighted_sum(credits, marks):
    return np.sum(credits * marks)

#Sort student list by GPA descending
def sort_students_by_gpa(students):
    gpas = np.array([student.gpa for student in students])
    sorted_indices = np.argsort(gpas)[::-1]
    sorted_students = [students[i] for i in sorted_indices]
    return sorted_students

#Display the sorted student list using curses
def display_sorted_student_list(students):
    print("Sorted Student List by GPA (Descending):")
    for student in students:
        print(f"{student.stud_name} - GPA: {student.gpa:.2f}")

def main():
    students = []  #Initialize a list to store student objects
    courses = []   #Initialize a list to store course objects

    #Input student information
    stud_number = int(input("Input number of students: "))
    for _ in range(stud_number):
        stud_id = input("Input student ID: ")
        stud_name = input("Input student name: ")
        stud_dob = input("Input student DoB: ")
        student = Student(stud_id, stud_name, stud_dob)
        students.append(student)

    #Input course information
    c_number = int(input("Input number of courses: "))
    for _ in range(c_number):
        c_id = input("Input course ID: ")
        c_name = input("Input course name: ")
        course = Course(c_id, c_name)
        courses.append(course)

    choice = -1
    marks = []

    while choice != 0:
        print("1. Select a course and input student marks ")
        print("2. Calculate GPA for each student and sort by GPA")
        print("3. Exit")
        print("Enter your choice: ")
        choice = int(input())

        if choice == 1:
            # Select a course
            chosen_course_id = Course_sel.choose_course(courses)
            # Input student marks for the chosen course
            marks = Course_sel.stud_mark(students, courses[chosen_course_id-1])
        elif choice == 2:
            # Calculate GPA for each student
            for student in students:
                student_marks = [mark[4] for mark in marks if mark[2] == student.stud_id]
                student.gpa = calculate_average_gpa(student_marks)
            # Sort students by GPA
            sorted_students = sort_students_by_gpa(students)
            # Display the sorted student list using curses
            display_sorted_student_list(sorted_students)
        elif choice == 0:
            print("Exiting...")
        else:
            print("Try again.")

main()