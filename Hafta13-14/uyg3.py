from abc import ABC, abstractmethod

# Ana sınıf
class NotHesaplama(ABC):
    def __init__(self, vize, final, but=None, proje=None):
        self.vize = vize
        self.final = final
        self.but = but
        self.proje = proje

    @abstractmethod
    def hesapla(self):
        pass


# Vize ve Final ile hesaplama
class VizeFinal(NotHesaplama):
    def hesapla(self):
        return self.vize * 0.4 + self.final * 0.6


# Vize ve But ile hesaplama
class VizeBut(NotHesaplama):
    def hesapla(self):
        if self.but is not None:
            return self.vize * 0.4 + self.but * 0.6
        else:
            raise ValueError("But notu gerekli!")


# Vize, Final ve Proje ile hesaplama
class VizeFinalProje(NotHesaplama):
    def hesapla(self):
        if self.proje is not None:
            return self.vize * 0.3 + self.final * 0.5 + self.proje * 0.2
        else:
            raise ValueError("Proje notu gerekli!")


# Vize, Final, But ve Proje ile hesaplama
class VizeFinalButProje(NotHesaplama):
    def hesapla(self):
        if self.but is not None and self.proje is not None:
            return self.vize * 0.2 + self.final * 0.3 + self.but * 0.3 + self.proje * 0.2
        else:
            raise ValueError("But ve Proje notlari gerekli!")


# Ana program
def ana_program():
    print("Not Hesaplama Sistemi")
    vize = float(input("Vize notunu giriniz: "))
    final = float(input("Final notunu giriniz: "))

    # Final notu 50'den düşükse büt notu istenir
    if final < 50:
        print("Final notu 50'den düşük, büt notu girmeniz gerekiyor.")
        but = float(input("Büt notunu giriniz: "))
    else:
        but = None

    proje = float(input("Proje notunu giriniz (Yoksa -1 giriniz): "))
    proje = None if proje == -1 else proje

    # Polymorphism kullanımı
    hesaplama_siniflari = []

    hesaplama_siniflari.append(VizeFinal(vize, final))
    if but is not None:
        hesaplama_siniflari.append(VizeBut(vize, final, but=but))
    if proje is not None:
        hesaplama_siniflari.append(VizeFinalProje(vize, final, proje=proje))
    if but is not None and proje is not None:
        hesaplama_siniflari.append(VizeFinalButProje(vize, final, but=but, proje=proje))

    print("\nHesaplama Sonuclari:")
    for sinif in hesaplama_siniflari:
        print(f"{sinif.__class__.__name__}: {sinif.hesapla():.2f}")


# Çalıştır
ana_program()
