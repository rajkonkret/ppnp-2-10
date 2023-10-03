# set, zbiór - przechowuje niepowtarzajace się elementy
# tracimy kolejnosc przy dodawaniu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # zamiana listy na zbiór
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))
zb2 = set()  # pusty zbiór
print(zb2)  # set()

zbior.add(33)  # add() - dodawnie elementu do zbioru
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}

zbior.remove(55)  # usunięcie po elemencie
print(zbior)

print(zbior.pop())  # usunięcie pierwszego elemntu, 33
print(zbior)
print(len(zbior))  # 6
zbior.pop()
zbior.pop()
print(zbior)
print(type(zbior))  # <class 'set'>

lista2 = list(zbior)
print(lista2)  # [11, 44, 18, 22]
# 11:30

zbior2 = {66, 11, 44, 18, 52, 62, 999, 999}
print(zbior2)  # {66, 18, 52, 999, 11, 44, 62}
print(type(zbior2))  # <class 'set'>

print(zbior | zbior2)  # {66, 999, 11, 44, 18, 52, 22, 62} suma zbiorów
print(zbior & zbior2)  # częśc wspolna {18, 11, 44}
print(zbior - zbior2)  # {22}
print(zbior2 - zbior)  # {66, 52, 62, 999}
print(zbior.difference(zbior2))
print(zbior2.difference(zbior))
# {22}
# {66, 52, 62, 999}
print(zbior)  # {11, 44, 18, 22}
print(zbior2)  # {66, 18, 52, 999, 11, 44, 62}
# {11, 44, 18, 22} - {66, 18, 52, 999, 11, 44, 62} = {22}
