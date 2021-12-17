import numpy as np
  
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix1 = list(map(int, input().split()))
matrix2 = list(map(int, input().split()))

value1 = np.array(matrix1).reshape(R, C)
value2 = np.array(matrix2).reshape(R, C)
print(value1,value2)
d=np.dot(value1,value2)
print("Dot product of matrix is",d )
