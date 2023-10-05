import pandas as pd

excel_data = pd.read_excel('sales.xlsx')
data = pd.DataFrame(excel_data)
print("The content is: \n", data)
#    Sales Date    Sales Person  Amount
# 0 2018-05-12      Sila Ahmed   60000
# 1 2019-12-06     Mir Hossain   50000
# 2 2020-08-09    Sarmin Jahan   45000
# 3 2021-04-07  Mahmudul Hasan   30000

print(data.values)
print(data.items)
print(data.columns)
