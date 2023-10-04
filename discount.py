from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2023-10-04
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2023-10-04 09:54:43.369748
print(type(time))  # <class 'datetime.datetime'>

print(time.hour)
print(today.day)
print(today.year)

formatted_date = datetime.now().strftime('%d/%m/%Y')
print(formatted_date)  # 04/10/2023

formatted_time = datetime.now().strftime("%H:%M")
print(formatted_time)  # 10:05

formatted_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)  # 2023-10-04 10:07:11

# days = 0, seconds = 0, microseconds = 0,
# milliseconds = 0, minutes = 0, hours = 0, weeks = 0
# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2023-10-05

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': today, 'price': 80.0},
    {'sku': 3, 'exp_date': tomorrow, 'price': 20.0},
    {'sku': 4, 'exp_date': today, 'price': 50},
]
print(products)

for product in products:
    print(product)  # {'sku': 3, 'exp_date': datetime.date(2023, 10, 5), 'price': 20.0}
    if product['exp_date'] != today:
        continue  # nie wykonuj kolejnych instrukcji z pętli, idź na początek pętli, weź kolejny element

    product['price'] *= 0.8
    print(f"""
    Price for sku= {product['sku']}
    is now {product['price']}""")
