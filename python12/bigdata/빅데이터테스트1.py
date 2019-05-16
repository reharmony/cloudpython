'''
Created on 2019. 4. 18.

@author: user
'''
import pandas as pd
import numpy as np

s = pd.Series([1,3,5,6,8]) # 순서대로 리스트 인덱스 부여

print(s)

dates = pd.date_range('2013-01-03', periods=6)
print(dates)

# 소켓 = pd.interval_range(start=1, end=10, freq=5,closed=None)
# print(소켓)

df = pd.DataFrame(np.random.randn(6,4),index=dates, columns=['A','B','C','D'])

print("\ndf\n", df)
print("\nhead\n",df.head(3))
print("\nindex\n",df.index)
print("\ncolumns\n",df.columns)
print("\nvalues\n",df.values)
print("\ndescribe\n",df.describe())
print("\nsort_values\n",df.sort_values(by='B',ascending=False))
print("\ndf['A']\n",df['A'])
print("\ndf[0:3]\n",df[0:3])





