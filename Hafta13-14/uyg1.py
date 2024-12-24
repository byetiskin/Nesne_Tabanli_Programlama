class Sekil:
    def alan_hesapla(self):
        raise NotImplementedError("Alt sınıflar bu metodu geçersiz kılmalı!")

class Dikdortgen(Sekil):
    def __init__(self, en, boy):
        self.en = en
        self.boy = boy

    def alan_hesapla(self):
        return self.en * self.boy

class Daire(Sekil):
    def __init__(self, yaricap):
        self.yaricap = yaricap
        
    def alan_hesapla(self):
        return self.yaricap * self.yaricap * 3

# Polymorphism örneği
dikdortgen = Dikdortgen(5, 10)
daire = Daire(7)

sekiller = [dikdortgen, daire]
for sekil in sekiller:
    print(f"{sekil.__class__.__name__} alanı: {sekil.alan_hesapla()}")
