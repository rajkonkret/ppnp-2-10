wiek = 47
rok = 2023
temp = 36.6  # float
wiek2 = 37.5

print(wiek)
print(type(wiek))  # <class 'int'>

print(5 * "wiek")  # wiekwiekwiekwiekwiek

print(wiek * rok)  # 95081
print(wiek + rok)
print(wiek - rok)
print(wiek / rok)  # 0.023232822540781017 float- zawsze wynikiem dzielenia jest float
print(wiek // rok)  # czesc całkowita z dzielenia 0
print(wiek % rok)  # modulo - reszta z dzielenia 47
print(5 % 2)  # 1 bo 2 * 2 = 4 - 5 = 1
print(wiek ** rok)  # potęgowanie

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - (5 * 43) + (4 / 2 + 4) / 2)  # -158.0

print(0.2 + 0.8)  # 1.0  float
print(0.2 + 0.7)  # 0.8999999999999999
# float - przechowywane w pamieci jako mantysta i wykładnik
# bład zaokrąglenia
print(0.3 + 0.6 + 0.7)  # 1.5999999999999999

# typ logiczne
# prawda, fałsz
# True, False
czy_znasz_pythona = False  # obowiązkowo z dużej litery
print(czy_znasz_pythona)  # False, True
print(int(czy_znasz_pythona))  # int() - zamiana(rzutowanie) na liczbę int
# 1 - True, 0 - False

x = 1
print(bool(x))  # bool() - zamiana na typ logiczny, True
x = 100
print(bool(x))  # True
x = -10
print(bool(x))  # True
x = 0
print(bool(x))  # False
x = 'radek'
print(bool(x))  # True
x = ''
print(bool(x))  # False

# and - i
print(True and True)
print(True and False)
print(False and True)
print(False and False)
# True
# False
# False
# False

# or - lub
print(True or True)
print(True or False)
print(False or True)
print(False or False)
# True
# True
# True
# False

# not - negacja
print(not True)
print(not False)
# False
# True
# 14:42
