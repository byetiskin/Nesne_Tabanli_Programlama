# Üst sınıf - Anne
class Anne:
    def __init__(self):
        self.sac_rengi = "Kahverengi"
        self.goz_rengi = "Yeşil"

    def bilgi_goster(self):
        print(f"Anne - Saç Rengi: {self.sac_rengi}, Göz Rengi: {self.goz_rengi}")

class Baba:
    def __init__(self):
        self.boy = 180

    def bilgi_goster(self):
        print(f"Baba - Boy: {self.boy}")

# Alt sınıf - Cocuk
class Cocuk(Anne, Baba):
    def __init__(self):
        # Anne sınıfının __init__ metodunu otomatik olarak çağırıyoruz
        Anne.__init__(self)
        Baba.__init__(self)
        # Çocuğun kendine ait ek özellikleri burada tanımlayabiliriz
        self.isim = "Ali"

    def bilgi_goster(self):
        print(f"Çocuk - İsim: {self.isim}, Saç Rengi: {self.sac_rengi}, Göz Rengi: {self.goz_rengi}, Boy: {self.boy}")

# Cocuk sınıfından bir nesne oluşturalım
cocuk = Cocuk()

# Çocuğun bilgilerini gösterelim
cocuk.bilgi_goster()

