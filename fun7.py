# ** argumenty słownikowe

def connect(**opcje):
    print(opcje)
    print(type(opcje))  # <class 'dict'>
    connect_param = {
        'host': "127.0.0.7",
        'port': '9090'
    }
    connect_param['pwd'] = opcje
    print(connect_param)
    print(connect_param['pwd']['klucz'])  # wartosc


# connect()  # {} słownik
# {klucz:wartosc}
# klucz=wartosc
connect(klucz='wartosc')  # {'klucz': 'wartosc'}
connect(a1="2", klucz='wartosc')  # {'a1': '2', 'klucz': 'wartosc'}
# {'host': '127.0.0.7', 'port': '9090', 'pwd': {'a1': '2', 'klucz': 'wartosc'}}
connect(a1="2", klucz='wartosc', a=98)
# {'host': '127.0.0.7', 'port': '9090', 'pwd': {'a1': '2', 'klucz': 'wartosc', 'a': 98}}
