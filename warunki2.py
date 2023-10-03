# python 3.10
# match case

lista = []
lang = input("Podaj znany Ci język programownia")

match lang.lower().replace(" ", ""):
    case "python":
        lista.append(lang)
    case "c++":
        lista.append(lang)
    case "java":
        lista.append(lang)
    case _: # wartość domyślna (odpowiednik else)
        print("nie znam takiego działania")

print(lista)
# usprawnić program tak aby spacje i duze/małe litery nie mialy znaczenia
