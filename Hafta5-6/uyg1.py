class Calisan:
    calisan_sayisi = 0  # Sınıf değişkeni

    def __init__(self, isim, maas):
        self.isim = isim
        self.maas = maas
        Calisan.calisan_sayisi += 1

    @classmethod
    def calisan_sayisini_goster(cls):
        # Sınıf değişkenine erişim sağlıyor ve toplam çalışan sayısını gösteriyor
        print(f"Toplam çalışan sayısı: {cls.calisan_sayisi}")

    @staticmethod
    def maas_hesapla(temel_maas, prim_orani):
        # Sınıf veya örneklem ile ilgisi yok, bağımsız bir işlem yapıyor
        return temel_maas + (temel_maas * prim_orani)

# Sınıftan birkaç örneklem oluşturalım
calisan1 = Calisan("Mert", 5000)
calisan2 = Calisan("Ayşe", 6000)

# Sınıf metodunu hem sınıf üzerinden hem de örneklem üzerinden çağırabiliriz
Calisan.calisan_sayisini_goster()  # Sınıf üzerinden çağrı
calisan1.calisan_sayisini_goster()  # Örneklem üzerinden çağrı

# Statik metodu hem sınıf üzerinden hem de örneklem üzerinden çağırabiliriz
print(Calisan.maas_hesapla(5000, 0.1))  # 5500
print(calisan1.maas_hesapla(4000, 0.2))  # 4800
