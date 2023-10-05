# pliki csv
# pliki tekstowe, gdzie dane oddzielone są seperatorem
# Radek, Maciek, Zenek
import csv

row = ['radek', 'coe', 3, '9.1']
fields = ['name', 'branch', 'year', 'cgpa']
dict2 = dict(zip(fields, row))
print(dict2)  # {'name': 'radek', 'branch': 'coe', 'year': 3, 'cgpa': '9.1'}

dict_x = [
    {'name': 'radek', 'branch': 'coe', 'year': 3, 'cgpa': '9.10'},
    {'name': 'Tomek', 'branch': 'cos', 'year': 2, 'cgpa': '9.0'},
    {'name': 'Kasia', 'branch': 'cor', 'year': 1, 'cgpa': '9'},
]

filename = 'records.csv'
with open(filename, 'w', encoding='utf-8', newline='') as csv_f:
    # csvwriter = csv.writer(csv_f)
    # csvwriter.writerow(row)  # zpisanie wiersza z listy
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields)
    csvwriter.writeheader()  # zapisanie nazw kolumn
    # csvwriter.writerow(dict2)  # zapisanie wiersza ze słownika
    csvwriter.writerows(dict_x)
