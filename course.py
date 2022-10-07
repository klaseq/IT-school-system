class Course:
    def __init__(self, name, teacher=None, students=None):
        self.name = name
        self.teacher = teacher
        self.students = students or []
    
    def add_student(self, student):
        self.students.append(student)
    
    def __str__(self):
        next_row = "\n\t"
        return f"Course {self.name}\n\t{self.teacher}\n\t{next_row.join([student.__str__() for student in self.students])}"