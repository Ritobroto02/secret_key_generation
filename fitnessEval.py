import random

l = []
m=[]

def my_list():
   
    for j in range(0,64):
     x = random.randint(0,1)
     l.append(x)
    
    return l

m.append(l)

def largest_row_of_zeros(l):

    c = 0
    max_count = 0

    for j in l:
        if j == 0:
            c += 1
        else:
            if c > max_count:
                max_count = c
            c = 0
    return max_count

def largest_row_of_ones(l):

    c = 0
    max_count = 0

    for j in l:
        if j == 1:
            c += 1
        else:
            if c > max_count:
                max_count = c
            c = 0
    return max_count

l = my_list()
print(largest_row_of_zeros(l))
print(largest_row_of_ones(l))

def avg():
 sum=largest_row_of_ones(l)+largest_row_of_zeros(l)
 a=sum/2
 return float(a)
     
print(avg())
print(m)