# ----------------------------------------------------------------
# Author: Steven Murphy
# Date: May 5, 2020
#
# This program creates a class registration system

from course import Course
from student import Student


def main():
    # ------------------------------------------------------------
    # This function manages the whole registration system.
    # It creates student list and course list. A loop serves multiple students.
    # Inside the loop, ask student to enter ID, and call the login function to verify
    # student's identity. Then let student choose to add course,
    # drop course or list courses. This function has no return value.
    # -------------------------------------------------------------

    course_list = []
    student_list = []
    init_lists(course_list, student_list)
    option = 0
    while option == 0:
        id = input("Enter ID to log in, or 0 to quit: ")
        if id == '0':
            print("Login Ended")
            break
        else:
            student = login(id, student_list)
            if student:
                print("ID and PIN verified")
                print()
                selection = 4
                while selection != 0:
                    selection = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to display course roster, 0 to exit: "))
                    if selection == 1:
                        student.add_course(course_list)
                        print()

                    elif selection == 2:
                        student.drop_course(course_list)
                        print()

                    elif selection == 3:
                        student.list_courses(course_list)
                        print()

                    #  elif selection == 4:

                    elif selection == 0:
                        print("Session ended")
                        print()
                        break


def login(id, s_list):
    # ------------------------------------------------------------
    # This function allows a student to log in.
    # if id and pin match it will
    # display message of verification and return that Student
    # object. Otherwise, display error message and return None.
    # -------------------------------------------------------------

    pin = input("Enter PIN: ")
    for student in s_list:
        if student.get_id() == id and student.get_pin() == pin:
            return student
    else:
        print("ID and PIN incorrect")
        return None


def init_lists(c_list, s_list):
    # ------------------------------------------------------------
    # This function adds elements to course_list and student_list.
    # This function has no return value.
    # -------------------------------------------------------------

    course1 = Course("CSC101", 3)
    course1.add_student("1004")
    course1.add_student("1003")
    c_list.append(course1)
    course2 = Course("CSC102", 2)
    course2.add_student("1001")
    c_list.append(course2)
    course3 = Course("CSC103", 1)
    course3.add_student("1002")
    c_list.append(course3)

    student1 = Student("1001", "111")
    s_list.append(student1)
    student2 = Student("1002", "222")
    s_list.append(student2)
    student3 = Student("1003", "333")
    s_list.append(student3)
    student4 = Student("1004", "444")
    s_list.append(student4)


main()
