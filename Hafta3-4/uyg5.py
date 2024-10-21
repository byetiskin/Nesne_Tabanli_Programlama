class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.grade = grade  

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if 0 <= grade <= 100:  # Geçerli bir not aralığı
            self._grade = grade
        else:
            raise ValueError("Not 0 ile 100 arasında olmalı")

try:
    student = Student("Ali", 140) 
    print(student.name)
    print(student.grade)
except ValueError as e:
    print(e)  
