import numpy as np

m = float(input('meu1 = '))
while m > 4:
    print('Enter within 0 to 4')
    m = float(input('meu1 = '))


x = np.array([float(input('x = '))])
while x[0] > m and x < 0:
    print('Enter within 0 to', m)
    x = np.array([float(input('x = '))])

n = int(input('Number of Bits = '))

for i in range(0,n):
    x = np.append(x, m*x[i]*(1-x[i]))
    print(x)