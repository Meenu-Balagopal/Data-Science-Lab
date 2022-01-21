import pandas as pd
df1=pd.read_csv("Program_4.7.csv")
print(df1) 
print()
df2 = df1.reset_index()
print(df2)