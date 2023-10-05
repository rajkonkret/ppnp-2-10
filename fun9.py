# lambda - skrócony zapis funkcji

def odejmij2(a, b):
    return a - b


odejmij = lambda a, b: a - b  # lambda zwraca wynik

print(odejmij2(7, 9))
print(odejmij(6, 2))

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))
print(wiek(12))
print(wiek(29))

lista = [1, 2, 3, 4, 8, 10, 23, 50]
l = []
for i in lista:
    l.append(i * 2)
print(l)  # [2, 4, 6, 8, 16, 20, 46, 100]
print([i * 2 for i in lista])  # [2, 4, 6, 8, 16, 20, 46, 100]


def zmien(x):
    return x * 2


# map() - zamiany damych wg zadanej funkcji
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 6, 8, 16, 20, 46, 100]
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map(): [2, 4, 6, 8, 16, 20, 46, 100]
# filter() - filtrowanie, zwraca elemnty spełniające warunek
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 8, lista))}")
# Zastosowanie filter(): [10, 23, 50]
# wyfiltrowac wieksze od 3
# wyfiltrowac x > 3 i x < 20
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 3, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 20, lista))}")
# x > 3 and x < 20 -> 3 < x < 20
# Zastosowanie filter(): [4, 8, 10]
