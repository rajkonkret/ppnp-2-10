# instrukcje warunkowe - instrukcja sterownia przepływem programu
# if
# sterowna warunkiem, jezeli warunek jest True to wykonuje działania z wydzielonego bloku
odp = False
if odp:
    print("Brawo")  # obowiazkowo wcięcie  (4 spacje), conajmniej jedna we wcieciu
else:  # w przeciwnym przypadku
    print("Musisz się dalej uczyc")
print("Działam dalej")

# podatek = 0.0
# zarobki = int(input("Podaj dochód"))
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:  # kolejny warunek, a jezeli nie to...
#     podatek = 0.4
# else:
#     podatek = 0.6
#
# print(podatek)
# print(f"Podatek wynosi {zarobki * podatek}")
# # dodac kolejny podatek (0.2) dla zarobków pomiedzy 10000 a 29999
# # kolejnosc warunków ma znaczenie

suma_zam = 100
if suma_zam > 150:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabat wynosi {rabacik}")  # f - string format

rabat = 25 if suma_zam > 150 else 0
print(f"Rabat wynosi {rabat}")  # f - string format

lista_bledow = []  # pusta lista
# alert_system = 'console'
alert_system = 'email'
# error = 'medium'
error = 'inny'
error_message = "Stało się coś strasznego"

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    lista_bledow.append("email")
    if error == 'medium':
        lista_bledow.append('ostrzeżenie')
    elif error == 'critical':
        lista_bledow.append("krytyczny")
    else:
        lista_bledow.append("inny błąd")
else:
    print("System nieznany")

# dodac błąd inny, wpisywac do listy "inny błąd"
print(lista_bledow)

a = 14
b = 3
print(f"Wynik porównania {a} > {b}, {a > b}")
print(f"Wynik porównania {a} < {b}, {a < b}")
print(f"Wynik porównania {a} >= {b}, {a >= b}")
print(f"Wynik porównania {a} <= {b}, {a <= b}")
print(f"Wynik porównania {a} == {b}, {a == b}")  # porównanie ==
print(f"Wynik porównania {a} != {b}, {a != b}")  # różne
# Wynik porównania 14 > 3, True
# Wynik porównania 14 < 3, False
# Wynik porównania 14 >= 3, True
# Wynik porównania 14 <= 3, False
# Wynik porównania 14 == 3, False
# Wynik porównania 14 != 3, True

# napisac test z historii, geografii, czegokolwiek
# wyswietlic pytanie (print)
# pobrac odpowiedz (input)
# sprawdzic odpowiedz i wypisac wynik (if else)

odp = input("Podaj date Chrztu Polski")
if odp == '966':
    print("Prawidłowa odpowiedź")
else:
    print("Masz w ksiązce na stronie 23")
# 13:20
