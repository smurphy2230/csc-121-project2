from course import Course


class Student(Course):

    def __init__(self, id, pin):
        super().__init__(id, pin)
        self.__id = id
        self.__pin = pin

    def get_id(self):

        return self.__id

    def get_pin(self):

        return self.__pin

    def add_course(self, c_list):

        input_course = input("Enter course you want to add: ").upper()
        count = 0
        for course in c_list:
            if course.get_course_code() == input_course:
                count += 1
                course.add_student(self.get_id())
        if count == 0:
            print("Course not found")

    def drop_course(self, c_list):

        drop_course = input("Enter course you to drop: ").upper()
        count = 0
        for course in c_list:
            if course.get_course_code() == drop_course:
                count += 1
                course.drop_student(self.get_id())
        if count == 0:
            print("Course not found")

    def list_courses(self, c_list):

        count = 0
        print("Course registered:")
        for course in c_list:
            if course.student_in_course(self.get_id()):
                print(course.get_course_code())
                count += 1
        print("Total number of courses registered: ",count)


