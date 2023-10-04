# napisac aplikacje kalkulator
# wykorzystac jako główną petle programu while
# pobrac rodzaj operacji, 5 wyjscie z programu
# pobrac liczby
# wyswietlic wynik
while True:
    print(f"""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    """)

    odp = input("Podaj operacje")  # str
    if odp > '4':  # porównujemy ze str '4'
        break
    try:
        a = float(input("Podaj pierwszą liczbę"))
        b = float(input("Podaj drugą liczbę"))  # ValueError: could not convert string to float: 'a'

        if odp == '1':
            print("Wynik", a + b)
        elif odp == '2':
            print("Wynik", a - b)
        elif odp == '3':
            print("Wynik", a * b)
        elif odp == '4':
            print("Wynik", a / b)  # ZeroDivisionError: float division by zero
        else:
            print("Nie znam takiego działania")
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except ValueError:
        print("Bład wartości")
    except Exception as e:  # łapie pozostałe wyjątki
        print("Bład", e)
    else:  # wykonuje się tylko, gdy nie ma błedu
        print("Gdy nie ma błedu")
    finally:
        print("Zawsze")  # wykonuje się zawsze

# 11:30 try except [else][finally]
