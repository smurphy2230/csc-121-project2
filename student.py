from course import Course


class Student(Course):

    def __init__(self, id, pin):
        super().__init__(id, pin)
        self._id = id
        self._pin = pin

    def getId(self):
        return self._id

    def getPin(self):
        return self._pin

    def addCourse(self, c_list):
        add_course = input("Enter the course you want to add: ").upper()
        c = 0
        for course in c_list:
            if course.getCourseCode() == add_course:
                c += 1
                course.addStudent(self.getId())
        if c == 0:
            print("Course not found")

    def dropCourse(self, c_list):
        drop_course = input("Enter the course you want to drop: ").upper()
        c = 0
        for course in c_list:
            if course.getCourseCode() == drop_course:
                c += 1
                course.dropStudent(self.getId())
        if c == 0:
            print("Course not found")

    def listCourses(self, c_list):
        c = 0
        print("Courses registered:")
        for course in c_list:
            if course.studentInCourse(self.getId()):
                print(course.getCourseCode())
                c += 1
                print("Total number of courses registered: ", c)


