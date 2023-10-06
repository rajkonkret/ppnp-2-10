class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    # print(2 / 0)
    raise MyException("Wystąpił wyjątek")  # MyException: Wystąpił wyjątek - rzucamy wyjatek
except MyException:
    print("Wystąpił wyjatek MyException")  # Wystąpił wyjatek MyException

except Exception as e:
    print("Błąd", e)  # Błąd Wystąpił wyjątek
