# klasa - szablon(formularz) wskazujący jakie cechy bedzi emiał obiekt
# cechy - pola (zmienne)
# działania - funkcje
# obiekt- budowany na podstawie klasy (instancja kalsy)

# definicja klasy
# PEP8 - wskzuje, ze nazwy klas z dużej litery
class Human:
    """
    Klasa opisująca człowieka w Pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(self)  # tylko wypisanie obiektu
        print(f"Nazywam się {self.imie}")

    def wypisz_wiek(self):
        print(f"Wiek: {self.wiek}")


print(Human.__doc__)  # wypisanie dokumentacji
# Klasa
# opisująca
# człowieka
# w
# Pythonie
print(print.__doc__)
# Prints the values to a stream, or to sys.stdout by default.
#
#   sep
#     string inserted between values, default a space.
#   end
#     string appended after the last value, default a newline.
#   file
#     a file-like object (stream); defaults to the current sys.stdout.
#   flush
#     whether to forcibly flush the stream.
help(print)  # wypisanie dokumentacji
cz1 = Human()  # tworzenie obiektu, uruchaianie klasy Human
print(cz1)  # <__main__.Human object at 0x0000022BD49BE590>
print(cz1.plec)  # k
cz1.imie = "Kasia"
cz1.wiek = 29
print(cz1.imie)
print(cz1.wiek)
cz1.powitanie()

# stworzyc inny obiekt innej płci
cz2 = Human()
cz2.imie = "Tomek"
cz2.wiek = 87
cz2.plec = "m"
print(cz2.imie)
cz2.powitanie()
# dopisac metode wypisz_wiek()
cz1.wypisz_wiek()
cz2.wypisz_wiek()
