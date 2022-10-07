from person import Student, Teacher
from course import Course

class ITSystem:
    def __init__(self, courses=None, students=None, teachers=None):
        self.courses = courses or []
        self.students = students or []
        self.teachers = teachers or []
    
    def create_student(self):
        print("student details:")
        while True:
            try:
                name=input("Name: ")
                surname=input("Surname: ")
                grade=input("Grade: ")
                print("Select your course:")
                for counter, course in enumerate(self.courses):
                    print(f"{counter}, {course}")
                course_id = int(input("Course id: "))
                if course_id < 0 or course_id >= len(self.courses):
                    raise Exception("Wrong course number, please try again")
            except Exception as e:
                print(e)
                print("Error during adding a student, please try again")
                continue
            break
        student=Student(name, surname, grade)
        self.courses[course_id].add_student(student)
        self.students.append(student)
        
    def create_teacher(self):
        print("teacher details: ")
        while True:
            try:
                name=input("Name: ")
                surname =input("Surname: ")
                degree=input("Degree:")
            except Exception as e:
                print(e)
                print("Error during adding a teacher, please try again")
                continue
            break
        teacher=Teacher(name, surname, degree)
        self.teachers.append(teacher)

    def create_course(self):
        print("Course details: ")
        while True:
            try:
                name=input("Name: ")
                counter=0
                print("Select your teacher")
                for teacher in self.teachers:
                    print(f"{counter}, {teacher}")
                    counter += 1
                teacher_id = int(input("Teacher id: "))
                if teacher_id < 0 or teacher_id >= len(self.teachers):
                    raise Exception("Wrong number of teacher, please ty again")
            except Exception as e:
                print(e)
                print("Error during adding a course, please try again")
                continue
            break
        course = Course(name, self.teachers[teacher_id])
        self.courses.append(course)