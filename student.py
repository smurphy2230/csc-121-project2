from course import Course


class Student(Course):

    """constructor"""
    #  Student class takes two arguments, id and pin
    #  two protected instance variables id and pin

    def __init__(self, id, pin):
        super().__init__(id, pin)
        self.__id = id
        self.__pin = pin

    # get_id method has no parameter. returns the value of instance variable id

    def get_id(self):

        return self.__id

    # get_pin method has no parameter. returns the value of instance variable pin

    def get_pin(self):

        return self.__pin

    #  add_course method has one parameter, c_list. Calls add_student method to add student
    #  to course if it's available

    def add_course(self, c_list):

        course_id = input("Enter course you want to add: ").upper()
        count = 0
        for course in c_list:
            if course.get_course_code() == course_id:
                count += 1
                course.add_student(self.get_id())
        if count == 0:
            print("Course not found")

    #  drop_course method has one parameter, c_list. Calls drop_student method to remove student
    #  from course if enrolled

    def drop_course(self, c_list):

        course_id = input("Enter course you to drop: ").upper()
        count = 0
        for course in c_list:
            if course.get_course_code() == course_id:
                count += 1
                course.drop_student(self.get_id())
        if count == 0:
            print("Course not found")

    #  list_courses method displays and counts courses a student is registered for. One parameter, c_list
    #  iterates over c_list to display and count courses

    def list_courses(self, c_list):

        count = 0
        print("Course registered:")
        for course in c_list:
            if course.student_in_course(self.get_id()):
                print(course.get_course_code())
                count += 1
        print("Total number of courses registered: ",count)


