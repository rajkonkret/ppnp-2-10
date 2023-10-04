# funkcje kantor
# usd, eur

def kantor(waluta):
    print("Uruchomienie kantoru")

    def usd(kwota=0):
        print(f"Wymieniam dolary: {kwota} usd = {int(kwota) * 4.3}")

    def eur(kwota=0):
        print(f"Wymieniam eur: {kwota} eur = {int(kwota) * 4.6}")

    if waluta == 'eur':
        return eur
    else:
        return usd


kantor_usd = kantor('usd')
print(kantor_usd)  # <function kantor.<locals>.usd at 0x000002917D2A8E00>
kantor_usd()
# prerobic tak by funkcje wewnetrzne przyjmowały kwote do wymiany
# Wypisac łądnie w postaci:
# Wymieniam dolary: 1000 usd = 4300 pln
kantor_usd(1000)  # Wymieniam dolary: 1000 usd = 4300.0
kantor_eur = kantor('eur')
kantor_eur(1000)  # Wymieniam eur: 1000 eur = 4600.0
