print()  # wypisz/wydrukuj
print("Nazywam się Radek")
print('Nazywam się Radek')
print('cos tam "cytat"')  # cos tam "cytat"
print("cos tam \"cytat\"")  # cos tam "cytat"
# komentarz
# ctrl / - zakomentowanie zaznaczonych linii
# type()  - wypisanie typu danych
print(type("Radek"))  # <class 'str'> string

print(39)
print(type(39))  # <class 'int'>
print("39")
print(type("39"))  # <class 'str'>

print("39" + "14")  # 3914
# konkatenacja tekstów (łączenie)
print(39 + 14)  # 53
print(5 * "4")  # 44444

# zmienna
# pudełko na dane
imie = "Radek"
print(imie)  # wypisujemy zawartość zmiennej a nie słowo imie
print(type(imie))  # <class 'str'>

imie = 48
print(imie)
print(type(imie))  # <class 'int'>

wiek = 48
print(wiek)
print(type(wiek))  # <class 'int'>

print(imie + wiek)  # 96
# print(5 + "4")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\ppnp-2-10\pierwszy.py", line 36, in <module>
#     print(5 + "4")
#           ~~^~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# int - integer - liczby całkowite
