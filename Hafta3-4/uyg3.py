# %% İlkel Tip
x = 10  # İlkel tip (integer)
y = x  # y, x'in değerini alır (kopyalama)

x = 20  # x'in değerini değiştirdik ama y hala 10
print(y)  # Çıktı: 10

# %% Referans Tip

a = [1, 2, 3]  # Referans tip (liste)
b = a  # b, a'nın referansını alır (aynı nesneyi paylaşır)

a.append(4)  # a'ya bir eleman ekliyoruz
print(b)  # Çıktı: [1, 2, 3, 4] - b de aynı nesneyi referansladığı için değişti

# %% Listeler

fruits = ["elma", "muz", "kiraz"]
fruits.append("portakal")  # Listenin sonuna eleman ekleme
fruits.remove("muz")  # Eleman silme

for fruit in fruits:
    print(fruit)
    
# %% Yığın

stack = []

# Yığına eleman ekleme (push)
stack.append(1)
stack.append(2)
stack.append(3)

# Yığından eleman çıkarma (pop)
print(stack.pop())
print(stack.pop())  
print(stack.pop())  

# %% Kuyruk

from collections import deque

queue = deque()

# Kuyruğa eleman ekleme (enqueue)
queue.append("Ali")
queue.append("Ayşe")
queue.append("Mehmet")

# Kuyruktan eleman çıkarma (dequeue)
print(queue.popleft())  
print(queue.popleft())  
print(queue.popleft())  

# %% Sözlük

# Sözlük oluşturma
student_grades = {"Ali": 85, "Ayşe": 92, "Mehmet": 78}

# Sözlüğe yeni eleman ekleme
student_grades["Fatma"] = 88

# Elemanları listeleme
for student, grade in student_grades.items():
    print(f"{student}: {grade}")

# Sözlükten eleman silme
del student_grades["Ali"]


