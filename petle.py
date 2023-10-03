# petle
# instrukcja sterowania przepływem
# for - petla iteracyjna
import random
from itertools import zip_longest

for i in range(10):  # 0..9
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # _ niema zmienna
    pass

lista2 = list(range(1, 50))  # 1..49
for i in range(6):
    wyn = random.choice(lista2)
    lista2.remove(wyn)
    print(wyn)

for i in range(10):
    print(i * 2)

for i in range(10):
    if i % 2 == 0:
        print(i, "Parzysta")
#
# 0 Parzysta
# 2 Parzysta
# 4 Parzysta
# 6 Parzysta
# 8 Parzysta

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]
lista4 = []
for j in range(10):
    if j % 2 == 0:
        lista4.append(j)

print(lista4)  # [0, 2, 4, 6, 8]

for c in lista4:
    if c == 2:
        c += 1  # c = c + 1
    print(c)  # 3

a = 1
a += 1  # a = a +1
print(a)  # 2
a -= 1  # a = a -1
print(a)  # 1
a *= 3  # a = a * 3
print(a)  # 3
a %= 2  # a = a % 2 reszta z dzielenia
print(a)  # 1
a /= 2  # a = a / 2
print(a)  # 0.5 float
# 14:35

imiona = ['Radek', 'Asia', 'Zbyszek', 'Karolina']
for p in imiona:
    print(p)

# wypisac imiona z tej listy
# 0 Radek
# 1 Asia

for p in range(len(imiona)):
    print(p, imiona[p])
# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Karolina

for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Karolina
# enumerate() - zwraca ponumerowane elementy kolekcji
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')  krotka
# (1, 'Asia')
# (2, 'Zbyszek')
# (3, 'Karolina')
a, b = (0, 'Radek')  # rozpakowanie krotki
print(a)
print(b)
for p, w in enumerate(imiona):
    print(p, w, sep=";", end='')  # 0;Radek1;Asia2;Zbyszek3;Karolina
# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Karolina
#  sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
print()

ludzie = ['Radek', 'Zenek', 'Andrzej', 'Karolina', 'Kasia']
wiek = [47, 67, 43, 32]

# wypisac osobe i odpowiadający jej wiek
# for p, o in enumerate(ludzie):
#     print(p, o, wiek[p])  # 3 Karolina 32
#     # IndexError: list index out of range
#     # bład przy róznych długościach list

# zip() - łaczy kolekcje
for k in zip(ludzie, wiek):
    print(k)  # ('Karolina', 32)
# o,w = k gdzie k to krotka ('Karolina', 32)
for o, w in zip(ludzie, wiek):
    print(o, w)
# Radek 47
# Zenek 67
# Andrzej 43
# Karolina 32
for p in enumerate(zip(ludzie, wiek)):
    print(p)  # (3, ('Karolina', 32))
# dla jednego elemntu
a, b = (3, ('Karolina', 32))
print(a, b)  # 3 ('Karolina', 32)
c, d = b  # ('Karolina', 32)
print(a, c, d)  # 3 Karolina 32

# analogicznie zrobic w petli tak by dla wszystkich elementow to sie wykonało (4)

for a, (c, d) in enumerate(zip(ludzie, wiek), start=1):  # start=1 numerowanie od 1 a nie od 0
    print(a, c, d)
# 0 Radek 47
# 1 Zenek 67
# 2 Andrzej 43
# 3 Karolina 32

jezyk = ['python', 'java']

zipped = zip_longest(ludzie, wiek, jezyk, fillvalue='Nan')
print(type(zipped))  # <class 'itertools.zip_longest'>
zipped_list = list(zipped)  # zamiana na liste

for item in zipped_list:
    print(item)
# ('Radek', 47, 'python')
# ('Zenek', 67, 'java')
# ('Andrzej', 43, 'Nan')
# ('Karolina', 32, 'Nan')
# ('Kasia', 'Nan', 'Nan')

for o, w, j in zipped_list:
    print(o, w, j)
# Radek 47 python
# Zenek 67 java
# Andrzej 43 Nan
# Karolina 32 Nan
# Kasia Nan Nan
