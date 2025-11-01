
#https://youtu.be/K5KVEU3aaeQ?si=r5OjGxrLwzIfjqk7
# ==================================================
import math

a = 22
b = 7

print(f"--- Bölme İşlemleri ---")
print(f"{a} / {b}  -> {a / b}")   # Normal Bölme (float)
print(f"{a} // {b} -> {a // b}")  # Kalansız bölme int
print(f"{a} % {b}  -> {a % b}")   # bölümden kalan

print(f"\n--- Üs Alma ---")
print(f"2 ** 3 -> {2 ** 3}")


# ==================================================
# Atamalar ve Math Fonksiyonları
# ==================================================

print(f"\n--- Arttırmalı Atama ---")
x = 10.5
print(f"x'in ilk değeri: {x}")
x += 5
print(f"x += 5 sonrası: {x}")

print(f"\n--- Yerleşik Math Fonksiyonları ---")
num = -2.9
print(f"abs({num})   -> {abs(num)}")
print(f"round({num}) -> {round(num)}")

print(f"\n--- 'math' Modülü ---")
num = 10.8
print(f"math.floor({num}) -> {math.floor(num)}")
print(f"math.ceil({num})  -> {math.ceil(num)}")


# ==================================================
# Input ve Tür Dönüşümü (Casting)
# ==================================================

# print(f"\n--- Kullanıcı Girdisi ---")
# y = input("Bir sayı girin: ")
# z = int(y) + 3 # str -> int dönüşümü
# print(f"İşlem sonucu: {z}, Türü: {type(z)}")


# ==================================================
# Koşullu İfadeler (if / elif / else)
# ==================================================

print(f"\n--- if/elif/else ---")
age = 20
print(f"Test edilen yaş: {age}")

if age > 21:
    message = "Koşul 1 (if)"
elif age >= 18:
    message = "Koşul 2 (elif)"
else:
    message = "Koşul 3 (else)"

print(f"Durum Mesajı: {message}")


# ==================================================
# Döngüler (Loops)
# ==================================================

print(f"\n--- for Döngüsü (range) ---")
# range(başlangıç, bitiş, artış)
for counter in range(1, 5, 1):
    print(f"Adım: {counter}, Çıktı: {'X' * counter}")


# ==================================================
# Fonksiyonlar (Functions)
# ==================================================

print(f"\n--- Basit Fonksiyon ---")

def add(number1, number2):
    return number1 + number2

toplam = add(23, 25)
print(f"add(23, 25) sonucu: {toplam}")


print(f"\n--- *args ile Fonksiyon ---")

def multiply_and_print(*numbers):
    print(f"Gelen Tuple: {numbers}")
    for number in numbers:
        print(f"  {number} * {number} = {number * number}")

multiply_and_print(2, 3, 4, 5)