# while - petla sterowana warunkiem
# instrukcja sterowania przepływem programu
# dopóki True pętla sie wykonuje

licznik = 0
while True:
    licznik += 1  # licznik = licznik + 1
    print("Komunikat!")
    if licznik > 10:
        break  # przerywa działąnie tej pętli

print(licznik)
print("Dalsza część programu.")
licznik = 0
while licznik < 11:
    print("Komunikat!!!")
    licznik += 1

lista = []
lista2 = []

while True:
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista2.append(int(wej))

print(lista)  # ['4', '5', '2', '12', '44']
print(lista2)  # [4, 5, 2, 12, 44]
