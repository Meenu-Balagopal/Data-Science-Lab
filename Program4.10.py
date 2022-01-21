import pandas as pd
df1=[[2,'Anu',49],[4,'Devika'],[8,'Manu'],[10,'Sona',50]]
df2=pd.DataFrame(df1,columns=['Rollno','Name','Mark'])
print(df2)
print("\nAfter Modification :: \n")
df3=df2.fillna(0)
df3