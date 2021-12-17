import matplotlib.pyplot as plt
x = []
y = []
for line in open('sample.txt', 'r'):
  lines = [i for i in line.split()]
  x.append(lines[0])
  y.append(int(lines[1]))
plt.title(" Mark Analysis")
plt.xlabel('Roll Number')
plt.ylabel('Marks')
plt.yticks(y)
plt.plot(x, y, marker = 'o', c = 'g')
plt.show()

