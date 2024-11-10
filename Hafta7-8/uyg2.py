class Calculator:
    # 1. Sınıfın Yapıcı Metodu 
    def __init__(self):
        self.result = 0  # Sınıf değişkeni: Hesaplama sonucunu tutar.

    # 2. Toplama Metodu
    def add(self, value):
        """Toplama işlemi: result += value"""
        self.result += value
        print(f"Eklendi: {value}. Şu anki sonuç: {self.result}")
        return self.result

    # 3. Çıkarma Metodu
    def subtract(self, value):
        """Çıkarma işlemi: result -= value"""
        self.result -= value
        print(f"Çıkarıldı: {value}. Şu anki sonuç: {self.result}")
        return self.result

    # 4. Çarpma Metodu
    def multiply(self, value):
        """Çarpma işlemi: result *= value"""
        self.result *= value
        print(f"Çarpıldı: {value}. Şu anki sonuç: {self.result}")
        return self.result

    # 5. Bölme Metodu
    def divide(self, value):
        """Bölme işlemi: result /= value"""
        if value != 0:
            self.result /= value
            print(f"Bölündü: {value}. Şu anki sonuç: {self.result}")
        else:
            print("Hata: Sıfıra bölme işlemi yapılamaz.")
        return self.result

calc = Calculator()
calc.add(10)        # Sonuç: 10
calc.subtract(5)    # Sonuç: 5
calc.multiply(3)    # Sonuç: 15
calc.divide(2)      # Sonuç: 7.5
