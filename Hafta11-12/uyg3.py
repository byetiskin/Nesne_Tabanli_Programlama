from abc import ABC, abstractmethod

# Abstract base class
class User(ABC):
    def __init__(self, name, id):
        self.name = name
        self.__id = id  # Private ID (encapsulation)

    def get_id(self):
        return self.__id  # Getter method for private ID

    @abstractmethod
    def introduce(self):
        pass

    @abstractmethod
    def task(self):
        pass

# Student class
class Student(User):
    def introduce(self):
        print(f"Merhaba, Ben {self.name}. Ben öğrenciyim. ID: {self.get_id()}")

    def task(self):
        print("Ders çalışıyorum.")

# Teacher class
class Teacher(User):
    def introduce(self):
        print(f"Merhaba, Ben  {self.name}. Ben öğretmenim. ID: {self.get_id()}")

    def task(self):
        print("Ders veriyorum.")


# Creating users
student1 = Student("Ali", 101)
teacher1 = Teacher("Ayse", 201)

student1.introduce()
student1.task()
print("------------")
teacher1.introduce()
teacher1.task()
