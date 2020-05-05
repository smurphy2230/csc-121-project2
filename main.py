# ----------------------------------------------------------------
# Author:
# Date: May 2, 2020
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------

from course import Course
from student import Student


def main():
    # ------------------------------------------------------------
    # This function manages the whole registration system.  It has
    # no parameter.  It creates student list and course list.  It
    # uses a loop to serve multiple students. Inside the loop, ask
    # student to enter ID, and call the login function to verify
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
            print("Ended")
            break
        else:
            return_student = login(id, student_list)
            if return_student:
                print("ID and PIN verified")
                print()
                option = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: "))
                while option in (1, 2, 3):
                    if option == 1:
                        return_student.add_course(course_list)
                        print()
                        option = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: "))

                    elif option == 2:
                        return_student.drop_course(course_list)
                        print()
                        choice = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: "))

                    elif option == 3:
                        return_student.list_courses(course_list)
                        print()
                        choice = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: "))

                if option == 0:
                    print("Session ended")
                    print()


def login(id, s_list):
    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination match the data of a Student object in s_list,
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
    # It makes testing and grading easier.  It has two parameters:
    # c_list is the list of Course objects; s_list is the list of
    # Student objects.  This function has no return value.
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
