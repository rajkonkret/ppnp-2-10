tekst = "Witaj świecie"
print(tekst)  # Witaj świecie
print(type(tekst))  # <class 'str'>

tekst2 = tekst.upper()  # zamiana tektu na duże litery
# przypisalismy do tekst2 wynik działania metody upper()
# """ Return a copy of the string converted to uppercase. """
print(tekst)  # Witaj świecie
print(tekst2)  # WITAJ ŚWIECIE
# teksty są immutable (niezmienne) niemutowalne
print(tekst.lower())  # witaj świecie

print(tekst.removeprefix("Witaj"))  # " świecie"
print(tekst.removesuffix("świecie"))  # "Witaj "
print(tekst.removesuffix("świecie").upper())  # "WITAJ "
print(tekst)  # Witaj świecie
# ctrl d - kopiowanie lini w ktorej ustawiony jest kursor

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'
print(type(encoded_s))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))  # Witaj świecie
# indeksowane od 0
print(tekst[0])  # W
print(tekst.count("i"))  # 3
print(tekst.count("i", 0, 4))  # 1
print(tekst.count("j", 0, 4))  # 0 z prawej strony zbior otwarty - 4 nie brane pod uwage
# Witaj świecie
# 01234

print(len(tekst))  # 13 długosc tekstu umieszczonego w tekst

imie = "Radek"
tekst_format = f"Mam na imie {imie} i lubię Pythona"  # Mam na imie Radek i lubię Pythona
print(tekst_format)
# f - fstringi - sformatowane stringi
# w {} umieszczamy nazwy zmiennych, których zawartość chcemy wyswietlic
tekst_format = f"\tMam na imie {imie}\n i lubię Pythona \b"
print(tekst_format)
# "	Mam na imie Radek
#  i lubię Pythona"
# \t tabulator
# \n nowa linia
# \b backspace

starszy = "Witaj %s"
# %s - oznacza wstaw w to miejsce string
print(starszy % imie)  # Witaj Radek

print("""
    Tekst
wielonijkowy""")
#     Tekst
# wielonijkowy

print("Witaj {}".format(imie))  # Witaj Radek
# 13:25
