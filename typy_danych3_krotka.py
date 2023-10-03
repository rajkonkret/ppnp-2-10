# krotka (tupla) - niezmienialna lista
# zmienna, niezmienna - jednoelementowa krotka
tupla = ("radek",)
print(type(tupla))  # <class 'tuple'>
print(tupla)
temp = 37, 5
print(type(temp))  # <class 'tuple'>
print((temp))  # (37, 5)

tupla2 = "Tomek", "Radek", "Zenek", "Marek"
tupla2a = ("Tomek", "Radek", "Zenek", "Marek")
print(type(tupla2))
print(type(tupla2a))  # <class 'tuple'>
print(tupla2)  # ('Tomek', 'Radek', 'Zenek', 'Marek')

# tupla równiez moze byc traktowana jako zmienna
tupla3 = 43, 55, 22.34, 11, 200
print(type(tupla3))

print(tupla2.index("Tomek"))  # 0
print(tupla2.count("Tomek"))  # 1

a, b = 1, 2
print(a)
print(b)
print(type((1, 2)))  # <class 'tuple'>
# rozpakowanie tupli
a, *b = 1, 2, 3  # * - worek na pozostałe elementy
print(a)  # 1
print(b)  # [2, 3]

print(tupla2)  # ('Tomek', 'Radek', 'Zenek', 'Marek')
imie1, *imie2, imie3 = tupla2
print(imie1)
print(imie2)
print(imie3)
# Tomek
# ['Radek', 'Zenek']
# Marek

lista = list(tupla3)  # zamiana (rzutowanie) tupli na liste
print(lista)  # [43, 55, 22.34, 11, 200]
print(type(lista))  # <class 'list'>
