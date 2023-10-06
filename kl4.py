class Dom:
    """
    klasa opisujące Dom
    """

    def __init__(self, metraz, kolor, liczba_okien):  # __init__ konstruktor
        # uzupełnic kontruktor
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    # stworzyc metody odczytujace te pola mam_kolor
    def mam_kolor(self):
        print(f"Mam kolor {self.__kolor}")

    def mam_metraz(self):
        print(f"Mam metraz {self.__metraz}")

    def mam_okna(self):
        print(f"Mam okien {self.__liczba_okien}")

    def zmien_kolor(self):
        wybor = input("Podaj kolor")
        self.__kolor = wybor
        self.mam_kolor()
        self.__farba()

    def zmien_okna(self):
        wybor = int(input("Podaj liczbę okien"))
        self.__liczba_okien = wybor
        self.mam_okna()

    def zmien_metraz(self):
        wybor = int(input("Podaj metraz"))
        self.__metraz = wybor
        self.mam_metraz()

    def __farba(self):
        print("Skończyła się farba")


dom1 = Dom(150, "biały", 10)
dom1.mam_okna()
dom1.mam_kolor()
dom1.mam_metraz()
# Mam okien 10
# Mam kolor biały
# Mam metraz 150
dom1.zmien_metraz()
dom1.zmien_kolor()
# Mam metraz 150
# Podaj metraz456
# Mam metraz 456
# Podaj kolorzielony
# Mam kolor zielony
# Skończyła się farba
