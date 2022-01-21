#Program 4.12

import pandas as pd

l1=[[100,'Arun',10000],[200,'Vivek',14000],[300,'Sona',9000]]
df1=pd.DataFrame(l1,columns=['eid','ename','stipend'])
print("\nDATAFRAME 1\n")
print(df1)

l2=[[100,'Teacher'],[200,'HOD'],[300,'Librarian']]
df2=pd.DataFrame(l2,columns=['eid','designation'])
print("\nDATAFRAME 2\n")
print(df2)

l3 = pd.merge(df1, df2, how = 'inner', on = 'eid') 
l3.rename(columns={'designation':'position'}, inplace = True)
print("\nMERGED DATAFRAME ")

