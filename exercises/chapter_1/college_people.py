# Construct a class hierarchy for people on a college campus. Include faculty, staff, and students. What do they have in common? What distinguishes them from one another?

class CollegePeople:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
class Faculty(CollegePeople):
    def __init__(self, name):
        super(Faculty, self).__init__(name)
        
        self.classes = None
        self.experience = None
        self.tenure = None

class Staff(CollegePeople):
    def __init__(self, name):
        super(Staff, self).__init__(name)
        
        self.job = None
        self.exerpience = None

class Student(CollegePeople):
    def __init__(self, name):
        super(Student, self).__init__(name)
        
        self.classes = None
        self.grade = None

