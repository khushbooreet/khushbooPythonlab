import pandas as pd

df = pd.read_csv('departments.csv')
sumgroup = df.groupby('DEPARTMENT_ID').sum()
print(sumgroup)

sumgroup.to_csv('khushboo.csv')
print("all data are instered in csv")
