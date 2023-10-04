# funkcja - wydzielony kod programu, ktory mozna wykonywac wielokrotnie

a = 6
b = 7


# definicja funkcji, tu funkcja sie nie wykonuje
def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj2(a, b):  # funkcja z dwoma argumentami, obowiązkowe a i b
    print(a + b)


def odejmij(a, b, c=0):  # argument c ma wartosc domyslna
    print(a - b - c)


def odejmij2(liczba1, liczba2):
    print(liczba1 - liczba2)


# wywołanie funkcji (uruchomienie)
dodaj()  # 13
dodaj2(6, 5)  # 11
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
odejmij(1, 2)
odejmij(1, 2, 7)  # przekazywani pozycyjne
odejmij(b=6, a=8, c=1)  # argumenty nazwane
odejmij(1, 2, c=8)
# odejmij(c=11, 2, 8)  # SyntaxError: positional argument follows keyword argument
odejmij2(4, 5)
odejmij2(liczba2=10, liczba1=25)
# print(dodaj() + dodaj2(5,7))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
print(dodaj())  # None
# funkcja nie zwraca wyniku (tylko wypisuje)
