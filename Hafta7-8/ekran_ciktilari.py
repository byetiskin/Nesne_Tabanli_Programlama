# %%
# 1
def list_sum(numbers):
    return sum(numbers)

print(list_sum([1, 2, 3, 4]))

# %%
# 2
def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))

# %%
# 3
def square(n):
    return n * n

print(square(5))

# %%
# 4
def max_of_three(a, b, c):
    return max(a, b, c)

print(max_of_three(3, 7, 5))

# %%
# 5
def is_even(n):
    return n % 2 == 0

print(is_even(8))  
print(is_even(7))  

# %%
# 6
def filter_even(numbers):
    return [n for n in numbers if n % 2 == 0]

print(filter_even([1, 2, 3, 4, 5, 6]))

# %%
# 7
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("radar"))  
print(is_palindrome("python"))  

# %%
# 8
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# %%
# 9
def count_occurrences(lst, target):
    return lst.count(target)

print(count_occurrences([1, 2, 3, 4, 1, 1, 2], 1))

# %%
# 10
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))

# %%
# 11
def check_sign(n):
    if n > 0:
        return "Pozitif"
    elif n < 0:
        return "Negatif"
    else:
        return "Sıfır"

print(check_sign(5))  
print(check_sign(-3)) 
print(check_sign(0))   

# %%
# 12
def to_uppercase(word):
    return word.upper()

print(to_uppercase("hello"))
# %%
# 13
class A:
    def __init__(self, num):
        num = 3
        self.num = num
    
    def change(self):
        self.num = 7

a = A(5)
print(a.num)  # Tahmin?
a.change()
print(a.num)  # Tahmin?

# %%
# 14
class B:
    num = 10  

    def __init__(self, num):
        self.num = num  

b = B(5)
print(B.num)  # Tahmin?
print(b.num)  # Tahmin?

# %%
# 15
class C:
    def __init__(self, value):
        self.value = value

    def double(self):
        return self.value * 2

    def update(self, new_value):
        self.value = new_value

c = C(4)
print(c.double())  # Tahmin?
c.update(10)
print(c.double())  # Tahmin?

# %%
# 16
class D:
    def __init__(self, items):
        self.items = items

    def add_item(self, item):
        self.items.append(item)

d = D([1, 2, 3])
print(d.items)  # Tahmin?
d.add_item(4)
print(d.items)  # Tahmin?

# %%
# 17
class E:
    def __init__(self, x=5):
        self.x = x

    def add(self, y):
        self.x += y

e = E()
print(e.x)  # Tahmin?
e.add(10)
print(e.x)  # Tahmin?

# %%
# 18
class F:
    def __init__(self, x):
        self.__x = x  

    def get_x(self):
        return self.__x

    def set_x(self, value):
        self.__x = value

f = F(5)
print(f.get_x())  # Tahmin?
f.set_x(10)
print(f.get_x())  # Tahmin?

# %%
# 19
class G:
    def __init__(self, value):
        self.value = value

g1 = G(5)
g2 = g1
g2.value = 10
print(g1.value)  # Tahmin?
print(g2.value)  # Tahmin?


