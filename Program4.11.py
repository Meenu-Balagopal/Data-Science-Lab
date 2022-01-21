import pandas as pd
df1=pd.read_csv("Program_4.11.csv")
print(df1)
df1['profit'] = df1['profit'].apply(lambda x:x>0)
df1