# Kitap sınıfı
class Book:
    def __init__(self, title, author):
        self.title = title  # Kitap adı
        self.author = author  # Kitap yazarı

    def get_info(self):
        return f"Kitap: {self.title}, Yazar: {self.author}"

# Kütüphane sınıfı
class Library:
    def __init__(self):
        self.books = []  # Kütüphanedeki kitapları saklayan liste

    # Kütüphaneye kitap ekleme
    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} adlı kitap kütüphaneye eklendi.")

    # Kütüphaneden kitap silme
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"{book.title} adlı kitap kütüphaneden silindi.")
                return
        print("Bu isimde bir kitap bulunamadı.")

    # Kütüphanedeki kitapları listeleme
    def list_books(self):
        if not self.books:
            print("Kütüphanede hiç kitap yok.")
        else:
            print("Kütüphanedeki kitaplar:")
            for book in self.books:
                print(book.get_info())

# Ana program
def library_system():
    library = Library()

    while True:
        print("\n--- Kütüphane Yönetim Sistemi ---")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitapları Listele")
        print("4. Çıkış")

        choice = input("Bir seçenek girin (1-4): ")

        if choice == "1":
            # Kitap ekle
            title = input("Kitap adı: ")
            author = input("Yazar adı: ")
            book = Book(title, author)
            library.add_book(book)

        elif choice == "2":
            # Kitap sil
            title = input("Silinecek kitabın adı: ")
            library.remove_book(title)

        elif choice == "3":
            # Kitapları listele
            library.list_books()

        elif choice == "4":
            # Çıkış
            print("Sistemden çıkılıyor.")
            break

        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

# Programı çalıştırma
library_system()  # Yorum satırından çıkardığınızda çalışır.
