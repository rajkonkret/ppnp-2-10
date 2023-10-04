# kalkulator na match case
while True:
    try:
        z = input("Podaj działanie + - * /")
        a = float(input("Podaj liczbę a"))
        b = float(input("Podaj liczbę b"))
        match z:
            case "+":
                print(f"Wynik dodawania {a} + {b} = {a + b}")
            case "-":
                print(f"Wynik odejmowania {a} - {b} = {a - b}")
            case "*":
                print(f"Wynik mnożenia {a} * {b} = {a * b}")
            case "/":
                print(f"Wynik dzielenia {a} / {b} = {a / b}")
            case _:
                break
    except ZeroDivisionError:
        print("Nie dzielimy przez zero")
    except ValueError:
        print("Bład wartości")
    else:
        print("Gdy nie ma błędu")
    finally:
        print("Zawsze")
