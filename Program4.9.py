#Program 4.9

import pandas as  pd
df1 =  pd.read_csv("Program_4.9.csv")
print(df1)
print("\n\n")
avg =  df1.groupby('Occupation')['Salary'].mean()
print(avg)