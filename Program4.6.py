# Program 4.6

import pandas as pd
df1=pd.read_csv("Program_4.6.csv")
print("Before Sorting \n")
print(df1)

print()
df2 = df1.sort_values(by = ['rollno']) 
print("After Sorting \n")
print(df2)