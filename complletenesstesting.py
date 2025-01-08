from itertools import count

import pandas as pd
from pandas import DataFrame
from pandas.core.algorithms import duplicated

df1 = pd.read_csv('departments.csv')
df2 = pd.read_csv('departments-2.csv')

#def metadata_check():
for col in df1.columns:
  if df1[col].dtype == df2[col].dtype:
        print("datatpe is matched",col,df1[col].dtype)

#print(df1['DEPARTMENT_NAME'].dtype)


#df1_dup = df1[df1['LOCATION_ID'].duplicated()]

#print(df1_dup)
#print(df1_dup.to_csv('reet.csv', index=False))
print(df1.groupby['location_id'].count())









