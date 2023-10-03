import random

# importowanie biblioteki random
# generowania liczb pseudolosowych

print(random.randint(1, 6))  # int 1..6
print(random.random())  # 0.3307210252084146 float 0..0.999999
print(random.random() * 6)  # 1.617472313677671 float 0..5.999999
print(random.randrange(6))  # int 0..5
print(random.randrange(1, 6))  # int 1..5

lista = [5, 7, 45, 34, 56]
print(random.choice(lista))

lista2 = list(range(1, 50))  # 1..49
print(lista2)
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
wyn = random.choice(lista2)  # losuje liczbe
lista2.remove(wyn)  # usuwa wylosowana liczby
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)

print(random.choices(lista2, k=6))  # [38, 18, 15, 5, 15, 36] - losuje z powtórzeniami
print(random.sample(lista2, 6))  # [13, 26, 20, 39, 43, 15] - bez powtórzeń
