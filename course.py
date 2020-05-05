class Course:

    """constructor"""

    def __init__(self, c_code, m_size):

        self._course_code = c_code
        self._max_size = m_size
        self._roster = []

    def add_student(self, id):

        if self._max_size == len(self._roster):
            print("Course already full")
        elif id in self._roster:
            print("You are already enrolled in this class")
        else:
            self._roster.append(id)
            print("Student: " + id + "added to: " + self._course_code)

    def drop_student(self, id):

        if id not in self._roster:
            print("You are not currently enrolled in this class")
        else:
            self._roster.remove(id)
            print("Student: " + id + "removed from: " + self._course_code)

    def get_course_code(self):

        return self._course_code

    def student_in_course(self, id):

        if id in self._roster:
            return True
        else:
            return False
