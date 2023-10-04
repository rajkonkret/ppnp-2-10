# napisz funkcję obliczjącą średnią

def liczby(i=0, *cyfry):
    print(cyfry)  # (1, 2, 3)
    suma = 0
    try:
        for c in cyfry:
            suma += c  # suma = suma + c
        count = len(cyfry)
        avg = suma / count
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Średnia dla ucznia {i} wynosi {avg}")


liczby()
liczby(1, 2, 3)
liczby(10, 2, 3, 4, 5, 6, 7, 8, 9)
liczby("Radek", 2, 3, 4, 5, 6, 7, 8, 9)
