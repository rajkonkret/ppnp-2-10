class Human:
    """
    klasa opisująca człowieka w Pythonie
    """

    # konstruktor (inicjalizator)
    def __init__(self, imie, wiek, wzrost, plec='k'):
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(self)  # tylko wypisanie obiektu
        print(f"Nazywam się {self.imie}")

    def wypisz_wiek(self):
        print(f"Wiek: {self.wiek}")

    def moj_wzrost(self):
        print(f"Moj wzrost wynosi", self.wzrost, "cm")

    def wypisz_plec(self):
        print(f"Płec: {self.plec}")

    def ruszaj(self):
        if self.plec == 'k':
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


cz1 = Human("Agata", 29, "178")
print(cz1.wiek)
print(cz1.imie)
print(cz1.wzrost)
print(cz1.plec)
# dopisac metode moj_wzrost
cz1.powitanie()
cz1.moj_wzrost()
cz1.ruszaj()

# drugi obiekt płci przeciwnej
cz2 = Human("Tomasz", 48, 190, "m")
cz2.powitanie()
cz2.ruszaj()
# 29
# Agata
# 178
# k
# <__main__.Human object at 0x00000113CAE02E90>
# Nazywam się Agata
# Moj wzrost wynosi 178 cm
# Ruszyłam w drogę
# <__main__.Human object at 0x00000113CAE02ED0>
# Nazywam się Tomasz
# Ruszyłem w drogę
cz1.wypisz_plec()
cz2.wypisz_plec()