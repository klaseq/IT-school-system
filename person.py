from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Student(Person):
    def __init__(self, name, surname, grade):
        super().__init__(name, surname)
        self.grade = grade
    
    def __str__(self):
        return f"Student: {self.name} {self.surname} grade {self.grade}"

class Teacher(Person):
    def __init__(self, name, surname, degree):
        super().__init__(name, surname)
        self.degree = degree
    
    def __str__(self):
        return f"Teacher: {self.name} {self.surname} {self.degree} degree"


