import pandas as pd

# pip install pandas

data = pd.read_csv('records.csv', delimiter=";")
print(data)
#     name branch  year  cgpa
# 0  radek    coe     3   9.1
# 1  Tomek    cos     2   9.0
# 2  Kasia    cor     1   9.0

print(data.columns)
print(data.values)
# Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
# [['radek' 'coe' 3 9.1]
#  ['Tomek' 'cos' 2 9.0]
#  ['Kasia' 'cor' 1 9.0]]
print(type(data.values))  # <class 'numpy.ndarray'>
print(data.values[0])  # ['radek' 'coe' 3 9.1]
print(data.items)
# <bound method DataFrame.items of     name branch  year  cgpa
# 0  radek    coe     3   9.1
# 1  Tomek    cos     2   9.0
# 2  Kasia    cor     1   9.0>
