# Üst sınıf - Benzinli Araç
class BenzinliArac:
    def __init__(self, yakit_deposu, yakit_tipi="Benzin"):
        self.yakit_deposu = yakit_deposu
        self.yakit_tipi = yakit_tipi
        self.yakit_miktari = yakit_deposu  # Başlangıçta depo dolu kabul edelim

    def benzin_doldur(self, miktar):
        self.yakit_miktari = min(self.yakit_deposu, self.yakit_miktari + miktar)
        print(f"Benzin dolduruldu. Mevcut yakıt miktarı: {self.yakit_miktari} litre")

    def yakit_durumu_goster(self):
        print(f"Yakit Tipi: {self.yakit_tipi}, Mevcut Yakıt: {self.yakit_miktari} litre")

    def motor_calistir(self):
        print("Benzinli motor çalıştırılıyor...")

# Üst sınıf - Elektrikli Araç
class ElektrikliArac:
    def __init__(self, batarya_kapasitesi):
        self.batarya_kapasitesi = batarya_kapasitesi
        self.sarj_durumu = 100  # Başlangıçta batarya tam dolu kabul edelim

    def sarj_et(self, miktar):
        self.sarj_durumu = min(100, self.sarj_durumu + miktar)
        print(f"Batarya şarj edildi. Mevcut şarj durumu: {self.sarj_durumu}%")

    def sarj_durumu_goster(self):
        print(f"Batarya Kapasitesi: {self.batarya_kapasitesi} kWh, Şarj Durumu: {self.sarj_durumu}%")

    def motor_calistir(self):
        print("Elektrikli motor çalıştırılıyor...")

# Çoklu kalıtım - Hibrit Araç
class HibritArac(BenzinliArac, ElektrikliArac):
    def __init__(self, yakit_deposu, batarya_kapasitesi):
        BenzinliArac.__init__(self, yakit_deposu)  # BenzinliArac sınıfının özelliklerini miras al
        ElektrikliArac.__init__(self, batarya_kapasitesi)  # ElektrikliArac sınıfının özelliklerini miras al

    def arac_bilgisi(self):
        print("Hibrit Araç Bilgileri:")
        self.yakit_durumu_goster()  # Benzinli aracın yakıt durumunu göster
        self.sarj_durumu_goster()  # Elektrikli aracın batarya durumunu göster

    def motor_calistir(self):
        # Hibrit araçlarda iki motor da bulunabilir, bu yüzden hangi motorun çalıştırılacağını belirtiyoruz
        if self.sarj_durumu > 0:
            ElektrikliArac.motor_calistir(self)  # Elektrikli motoru çalıştır
        elif self.yakit_miktari > 0:
            BenzinliArac.motor_calistir(self)  # Benzinli motoru çalıştır
        else:
            print("Yetersiz enerji! Lütfen yakıt veya şarj ekleyin.")

# Hibrit Araç örneği oluşturalım
toyota_prius = HibritArac(40, 15)

# Aracın bilgilerini ve durumunu gösterelim
toyota_prius.arac_bilgisi()

# Motoru çalıştıralım
toyota_prius.motor_calistir()

# Aracı şarj edelim ve tekrar kontrol edelim
toyota_prius.sarj_et(10)
toyota_prius.sarj_durumu_goster()

# Benzin dolduralım ve durumu tekrar gösterelim
toyota_prius.benzin_doldur(20)
toyota_prius.yakit_durumu_goster()
