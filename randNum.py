import numpy as np
import random

def randomIntFloat():
    guess = ['float', 'integer']
    x = random.choice(guess)

    if (x == 'integer'):
        num = random.randint(0, 4)
    else:
        num = random.uniform(0, 4)
    numarr=np.array(num)
    return print('',numarr)

n = int(input('Size of the population = '))
for i in range(n) or n>1:
    randomIntFloat()