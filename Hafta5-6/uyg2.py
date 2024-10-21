# Üst sınıf
class Hayvan:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
    
    def ses_cikar(self):
        print("Bu hayvan bir ses çıkarıyor.")

    def bilgi(self):
        print(f"İsim: {self.isim}, Yaş: {self.yas}")

# Alt sınıf - Kedi
class Kedi(Hayvan):
    def __init__(self, isim, yas, tuy_renk):
        super().__init__(isim, yas)  # Üst sınıfın (Hayvan) özelliklerini miras al
        self.tuy_renk = tuy_renk
    
    def ses_cikar(self):
        print("Miyav!")

    def bilgi(self):
        super().bilgi()  # Üst sınıftaki bilgi metodunu çağır
        print(f"Tüy Rengi: {self.tuy_renk}")


kedi = Kedi("Minik", 2, "Sarı")
kedi.bilgi()
kedi.ses_cikar()
