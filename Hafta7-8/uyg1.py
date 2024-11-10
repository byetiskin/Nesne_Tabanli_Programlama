class Television:
    def __init__(self):
        self.is_on = False  # TV varsayılan olarak kapalı
        self.channel = 1    # Varsayılan kanal
        self.volume = 5     # Varsayılan ses seviyesi
    
    def turn_on(self):
        """TV'yi aç."""
        if not self.is_on:
            self.is_on = True
            print("TV açıldı.")
        else:
            print("TV zaten açık.")

    def turn_off(self):
        """TV'yi kapat."""
        if self.is_on:
            self.is_on = False
            print("TV kapatıldı.")
        else:
            print("TV zaten kapalı.")

    def change_channel(self, channel):
        """Kanal değiştir."""
        if self.is_on:
            if 1 <= channel <= 100:
                self.channel = channel
                print(f"Kanal {self.channel} olarak değiştirildi.")
            else:
                print("Geçersiz kanal. Lütfen 1 ile 100 arasında bir kanal seçin.")
        else:
            print("Kanal değiştirilemez. TV kapalı.")

    def increase_volume(self):
        """Sesi artır."""
        if self.is_on:
            if self.volume < 10:
                self.volume += 1
                print(f"Ses seviyesi {self.volume} olarak artırıldı.")
            else:
                print("Ses seviyesi maksimumda.")
        else:
            print("Ses artırılamaz. TV kapalı.")

    def decrease_volume(self):
        """Sesi azalt."""
        if self.is_on:
            if self.volume > 0:
                self.volume -= 1
                print(f"Ses seviyesi {self.volume} olarak azaltıldı.")
            else:
                print("Ses seviyesi minimumda.")
        else:
            print("Ses azaltılamaz. TV kapalı.")
            

tv = Television()
tv.turn_on()  # TV açılır
tv.change_channel(45)  # Kanal 45'e değiştirilir
tv.increase_volume()  # Ses seviyesi artırılır
tv.decrease_volume()  # Ses seviyesi azaltılır
tv.turn_off()  # TV kapatılır

