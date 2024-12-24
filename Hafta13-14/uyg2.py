class Araba:
    def ses_cikar(self):
        raise NotImplementedError("Alt sınıflar bu metodu geçersiz kılmalı!")

class Sedan(Araba):
    def ses_cikar(self):
        return "Sedan: Brrr..."

class SUV(Araba):
    def ses_cikar(self):
        return "SUV: Vroom!"

# Polymorphism örneği
arabalar = [Sedan(), SUV()]

for araba in arabalar:
    print(araba.ses_cikar())
