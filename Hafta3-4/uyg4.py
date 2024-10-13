class Student:

    # Özellikler (Attributes)
    def __init__(self, name, grade, age):
        self.name = name  # Public: Her yerden erişilebilir
        self._age = age  # Protected: Yalnızca sınıf içinden ve alt sınıflardan erişilebilir
        self.__grade = grade  # Private: Yalnızca sınıfın içinden erişilebilir
    
    # Public metot: Öğrencinin adı ve notunu döndürür
    def get_info(self):
        return f"Öğrenci: {self.name}, Notu: {self.__get_grade()}"
    
    # Public metot: Öğrencinin geçip geçmediğini kontrol eder
    def is_passing(self):
        if self.__grade >= 50:  # Private değişken sınıf içinden erişilir
            return True
        else:
            return False
    
    # Protected metot: Öğrencinin yaşını değiştirmek için kullanılır
    def _change_age(self, new_age):
        self._age = new_age  # Protected değişken sınıf içinden ve alt sınıflardan değiştirilebilir
    
    # Private metot: Öğrencinin notunu döndürür
    def __get_grade(self):
        return self.__grade  # Private değişken sınıf içinden erişilebilir


# Öğrenciler listesi (dizi)
students = [
    Student("Ali", 45, 20),
    Student("Ayşe", 75, 22),
    Student("Mehmet", 60, 21)
]

# Döngü ile öğrenci bilgilerini ve geçme durumlarını kontrol edelim
for student in students:
    print("-------------")
    print(student.get_info())  # Public metot aracılığıyla bilgi alınır (Erişilebilir)
    
    if student.is_passing():  # Public metot aracılığıyla geçme durumu kontrol edilir (Erişilebilir)
        print(f"{student.name} dersi geçti.")  
    else:
        print(f"{student.name} dersi geçemedi.")
        
    # Aşağıdaki durumlar erişim kontrolü içindir:

    # Public değişken: name her yerden erişilebilir
    print(f"Erişilebilen public değişken - Adı: {student.name}")  # Bu çalışır
    
    # Protected değişken: _age dışarıdan erişilebilir, ama önerilmez
    print(f"Erişilebilen protected değişken - Yaşı: {student._age}")  # Bu çalışır ama önerilmez
    
    # Private değişken: __grade dışarıdan erişilemez
    try:
        print(f"Private değişken - Notu: {student.__grade}")  # Bu çalışmaz, hata verir
    except AttributeError:
        print("Private değişkene dışarıdan erişilemiyor: __grade")

    # Protected metot: _change_age dışarıdan erişilebilir, ama önerilmez
    student._change_age(25)  # Bu çalışır ama önerilmez
    print(f"Protected metotla yaşı değiştirildi: {student._age}")

    # Private metot: __get_grade dışarıdan erişilemez
    try:
        print(student.__get_grade())  # Bu çalışmaz, hata verir
    except AttributeError:
        print("Private metoda dışarıdan erişilemiyor: __get_grade")

