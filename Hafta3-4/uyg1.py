class Student:
    
    # Özellikler (Attributes)
    def __init__(self, name, grade):
        self.name = name  # Öğrencinin adı
        self.grade = grade  # Öğrencinin notu

    # Metotlar (Methods)
    def get_info(self):
        return f"Öğrenci: {self.name}, Notu: {self.grade}"

    # Öğrencinin geçip geçmediğini kontrol eden bir metot
    def is_passing(self):
        if self.grade >= 50:  # Eğer not 50 ve üzeriyse geçmiştir
            return True
        else:
            return False

# Öğrenciler listesi (dizi)
students = [
    Student("Ali", 45),
    Student("Ayşe", 75),
    Student("Mehmet", 60)
]

# Döngü kullanarak öğrencilerin bilgilerini ve geçme durumlarını kontrol edelim
for student in students:
    print(student.get_info())
    if student.is_passing():
        print(f"{student.name} dersi geçti.")
    else:
        print(f"{student.name} dersi geçemedi.")
