class Course:

    """constructor"""
    #  2 private arguments c_code and m_size
    #  3 private instance variables course_code, max_size, roster

    def __init__(self, c_code, m_size):

        self._course_code = c_code
        self._max_size = m_size
        self._roster = []

    #  add_student method with one parameter, id
    #  this method adds a student to the course roster. no return value

    def add_student(self, id):

        if self._max_size == len(self._roster):
            print("Course already full")
        elif id in self._roster:
            print("You are already enrolled in this class")
        else:
            self._roster.append(id)
            print("Student " + id + " added to " + self._course_code)

    #  drop_student method with one parameter, id
    #  this method drops a student from the course roster. no return value

    def drop_student(self, id):

        if id not in self._roster:
            print("You are not currently enrolled in this class")
        else:
            self._roster.remove(id)
            print("Student " + id + " removed from " + self._course_code)

    #  display_roster method sorts and displays the ID of students enrolled
    #  in a course. No parameter and no return value

    #  def display_roster(self):
        #  print("Enter course you want to see the roster of: ")
        #  new_roster = []
        #  c = 0
        #  for id in self._roster:
        #      new_roster.append(id)
        #      c += 1
        #  print(new_roster, c)

    #  get_course_code returns the value of self._course_code

    def get_course_code(self):

        return self._course_code

    # student_in_course method tests whether a student is enrolled. It has one parameter, id
    # returns True if enrolled, False if not enrolled

    def student_in_course(self, id):

        if id in self._roster:
            return True
        else:
            return False
