class Student:
    def __init__(self, name, grade):
        self.__name = name  # Private değişken
        self._grade = grade  # Protected değişken

    # Getter for name
    @property
    def name(self):
        return self.__name

    # Setter for name
    @name.setter
    def name(self, name):
        self.__name = name

    # Getter for grade
    @property
    def grade(self):
        return self._grade

    # Setter for grade
    @grade.setter
    def grade(self, grade):
        if 0 <= grade <= 100:  # Geçerli bir not aralığı
            self._grade = grade
        else:
            raise ValueError("Not 0 ile 100 arasında olmalı")

# Kullanım
student = Student("Ali", 85)
print(student.name)  # Ali
print(student.grade)  # 85

student.name = "Ayşe"
print(student.name)  # Ayşe
student.grade = 90
print(student.grade)  # 90

# Geçersiz bir not atanıyor
try:
    student.grade = 120  # ValueError: Not 0 ile 100 arasında olmalı
except ValueError as e:
    print(e)