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
