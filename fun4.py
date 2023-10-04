# funkcje zagnieżdzone

def fun1():
    print("To jest fun1")

    def fun2():  # to jest tylko deklaracja funkcji
        print("To jest fun2")

    return fun2  # zwracamy adres funkcji fun2


x = fun1()  # To jest fun1
print(x)  # <function fun1.<locals>.fun2 at 0x000001E7A1D38E00>
print(type(x))  # <class 'function'>
x()  # To jest fun2
