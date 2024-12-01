from abc import ABC, abstractmethod

# Soyut sınıf
class OdemeYontemi(ABC):
    @abstractmethod
    def odemeYap(self, tutar):
        pass  # Her alt sınıf bu metodu tanımlamak zorunda.

# Kredi Kartı ile ödeme
class KrediKarti(OdemeYontemi):
    def odemeYap(self, tutar):
        print(f"Kredi kartıyla {tutar} TL ödeme yapıldı.")

# Banka Havalesi ile ödeme
class BankaHavalesi(OdemeYontemi):
    def odemeYap(self, tutar):
        print(f"Banka havalesi ile {tutar} TL ödeme yapıldı.")

# Örnek kullanım:
def odemeYap(ödeme_yöntemi, tutar):
    ödeme_yöntemi.odemeYap(tutar)

# Ödeme Yöntemlerini Kullanma
kredi_karti = KrediKarti()
banka_havalesi = BankaHavalesi()

odemeYap(kredi_karti, 150)  # "Kredi kartıyla 150 TL ödeme yapıldı."
odemeYap(banka_havalesi, 300)  # "Banka havalesi ile 300 TL ödeme yapıldı."
