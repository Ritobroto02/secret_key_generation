import numpy as np
import random
import math
import statistics


def runsTest(l, l_median):

	runs, n1, n2 = 0, 0, 0
	
	# Checking for start of new run
	for i in range(len(l)):
		
		# no. of runs
		if (l[i] >= l_median and l[i-1] < l_median) or \
				(l[i] < l_median and l[i-1] >= l_median):
			runs += 1
		
		# no. of positive values
		if(l[i]) >= l_median:
			n1 += 1
		
		# no. of negative values
		else:
			n2 += 1

	runs_exp = ((2*n1*n2)/(n1+n2))+1
	stan_dev = math.sqrt((2*n1*n2*(2*n1*n2-n1-n2))/ \
					(((n1+n2)**2)*(n1+n2-1)))

	z = (runs-runs_exp)/stan_dev

	return z
	

def randomIntFloat():
    guess = ['float', 'integer']
    x = random.choice(guess)

    if (x == 'integer'):
        num = random.randint(0, 4)
    else:
        num = random.uniform(0, 4)
    numarr=np.array(num)
    return numarr
l=[]
n = int(input('Size of the population = '))
for i in range(n) or n>1:
    l.append(randomIntFloat())

print(l)

l_median= statistics.median(l)

Z = abs(runsTest(l, l_median))

print('Z-statistic= ', Z)




