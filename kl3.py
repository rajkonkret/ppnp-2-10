class Car:
    """
    Klasa samochód
    """

    def __init__(self, model, year):  # konstruktor
        self.model = model
        self.year = year
        self.__predkosc = 0  # __ - pole prywatne

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi: {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10


car1 = Car("Fiat", 2023)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(car1.__predkosc)  # 50 - odczytujemy pole predkosc
# nie odczytamy bo zostało oznaczone jako prywatne
car1.licznik()  # Prędkość wynosi: 50 km/h
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()  # Prędkość wynosi: 0 km/h
car1.__predkosc = 100  # nie robimy tak
car1.licznik()  # Prędkość wynosi: 100 km/h, Prędkość wynosi: 0 km/h - po zmianie na pole prywatne
