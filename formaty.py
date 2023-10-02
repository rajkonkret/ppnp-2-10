import sys

user = "Tomek"  # str
wiek = 39  # int
wersja = 3.110001  # float - liczby zmiennoprzecinkowe
liczba = 134567456234  # int
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)

print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308,
#                max_exp=1024,
#                max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15,
#                mant_dig=53, epsilon=2.220446049250313e-16,
#                radix=2, rounds=1)

print("Witaj %s masz teraz %d lat" % (user, wiek))  # Witaj Tomek masz teraz 39 lat
# print("Witaj %s masz teraz %d lat" % (wiek, user))  # TypeError: %d format: a real number is required, not str
# %s - str
# %d - digit - liczby
# przy konwencji z % python weryfikuje typ danych
print("Witaj %(user)s, masz teraz %(age)d lat." % {"user": user, "age": wiek})
# Witaj Tomek, masz teraz 39 lat.

print("Witaj {} masz teraz {} lat.".format(user, wiek))
print("Witaj {} masz teraz {} lat.".format(wiek, user))
# Witaj Tomek masz teraz 39 lat.
# Witaj 39 masz teraz Tomek lat.
# przy takim zapisie nie sprawdza typów
print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.
# f - fstring - tekst sformatowany {} dla zmiennych

print("Uzywamy wersji Pythona %i" % 3)
print("Uzywamy wersji Pythona %f" % 3.11)  # Uzywamy wersji Pythona 3.110000
print("Uzywamy wersji Pythona %.1f" % 3.11)  # Uzywamy wersji Pythona 3.1
print("Uzywamy wersji Pythona %.2f" % 3.11)  # Uzywamy wersji Pythona 3.11
print("Uzywamy wersji Pythona %.0f" % 3.11)  # Uzywamy wersji Pythona 3
print("Uzywamy wersji Pythona %.f" % 3.11)  # Uzywamy wersji Pythona 3
print("Uzywamy wersji Pythona %.f" % 3.9)  # Uzywamy wersji Pythona 4
# zero miejsc po przecinku zaokrągla podczas wyświetlania
x = 3.14
print("Zero miejsc po przecinku %.f" % x)
print("Oryginalny x =", x)
# Zero miejsc po przecinku 3
# Oryginalny x = 3.14

print(f"Używamy wersji Pythona {wersja}")  # Używamy wersji Pythona 3.110001
print(f"Używamy wersji Pythona {wersja:.1f}")  # Używamy wersji Pythona 3.1
print(f"Używamy wersji Pythona {wersja:.0f}")  # Używamy wersji Pythona 3

print(f"{user:>10}")  # "     Tomek" - uzupełniło spacjami z lewej strony do 10 znaków
print(f"{user:>20}")  # "               Tomek"
print(f"{user:<30}")  # "Tomek                         " z prawej strony uzupełnia
print(f"{user:^10}")  # "  Tomek   " wysrodkowanie

print(liczba)  # 134567456234
print("Nasza duża liczba {:,}".format(liczba))
# Nasza duża liczba 134,567,456,234
print("Nasza duża liczba {:,}".format(liczba).replace(",", "."))
print("Nasza duża liczba {:,}".format(liczba).replace(",", " "))
# Nasza duża liczba 134.567.456.234
# Nasza duża liczba 134 567 456 234
print(f"Nasza duża liczba {liczba:,}")
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))
# Nasza duża liczba 134,567,456,234
# Nasza duża liczba 134 567 456 234
# ctrl alt l - wyrównaie tekstu
