import csv

filename = 'records.csv'

fields = []
rows = []

with open(filename, 'r') as csv_f:
    # wyszukanie automatyczne seperatora dla csv
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)  # ;
    print(dialect)  # <class 'csv.Sniffer.sniff.<locals>.dialect'
    csv_f.seek(0)  # powrót na początek danych, ustawiamy licznik na 0
    # csvreader = csv.reader(csv_f, delimiter=";")
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)

    print(csvreader)  # <_csv.reader object at 0x0000018A1DF673A0>

    fields = next(csvreader)  # odcyt pierwszego wiersza i ustawienie licznika na nastepny
    for row in csvreader:  # pętla startuje od indeksu 1, czyli drugiego wiersza
        rows.append(row)

print(fields)
print(rows)
# ['name;branch;year;cgpa']
# [['radek;coe;3;9.10'], ['Tomek;cos;2;9.0'], ['Kasia;cor;1;9']]
# ['name', 'branch', 'year', 'cgpa']
# [['radek', 'coe', '3', '9.10'], ['Tomek', 'cos', '2', '9.0'], ['Kasia', 'cor', '1', '9']]
# 11:20
