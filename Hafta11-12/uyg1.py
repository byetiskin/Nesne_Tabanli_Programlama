from abc import ABC, abstractmethod # python içerisinde bulunan abstract modülü import ediyoruz

class UlasimAraci(ABC):  # Soyut sınıf
    @abstractmethod
    def calis(self):
        pass  # "Ne yapmalı" tarif edilir ama "Nasıl" belirtilmez.

    @abstractmethod
    def durdur(self):
        pass

# Alt sınıflar bu kurallara uymak zorunda:
class Araba(UlasimAraci):
    def calis(self):
        print("Arabayı anahtarla çalıştırdım.")

    def durdur(self):
        print("Arabayı durdurdum.")

class Bisiklet(UlasimAraci):
    def calis(self):
        print("Bisikleti pedal çevirerek çalıştırdım.")

    def durdur(self):
        print("Bisikleti durdurdum.")

# Kullanım:
araba = Araba()
araba.calis()  # Arabayı anahtarla çalıştırdım.
araba.durdur()    # Arabayı durdurdum.

bisiklet = Bisiklet()
bisiklet.calis()  # Bisikleti pedal çevirerek çalıştırdım.
bisiklet.durdur()    # Bisikleti durdurdum.
