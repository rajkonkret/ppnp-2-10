# klasa abstrakcyjna - klasa z której nie mozna stworzyc obiektu
from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "lecę z szybkością", self.szybkosc)

    @abstractmethod  # oznaczylismy metode jako abstrakcyjną
    def wydaj_odglos(self):
        pass


class Kura(Ptak):  # dziedziczenie po Ptaku
    """
    Kura
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)
        self.gatunek = gatunek

    def latam(self):
        print(f"Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("kokokokokokoko")


class Orzel(Ptak):
    """
    Orzel
    """

    def wydaj_odglos(self):
        print(f"piiiiiiiii")


# po dodaniu @abstractmethod klasa Ptak staje sie abstrakcyjna bo posiada metode abstrakcyjna
# TypeError: Can't instantiate abstract class Ptak with abstract method wydaj_odglos
# nie mozna utworzyc obiektu takiej klasy
# orz1 = Ptak("Orzeł", 20)
# orz1.latam()  # Tu orzeł lecę z szybkością 20
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura lecę z szybkością 0
# kur1.wydaj_odglos()

kur2 = Kura("Kura")
print(kur2.gatunek)
kur2.latam()  # Tu Kura Ja nie latam
kur2.wydaj_odglos()  # kokokokokokoko
orz2 = Orzel("Orzel", 34)
orz2.latam()
orz2.wydaj_odglos()  # piiiiiiiii
# 11:30
