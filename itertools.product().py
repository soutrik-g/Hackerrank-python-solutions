from itertools import product
a = input().split()
a = list(map(int,a))
b = input().split()
b = list(map(int, b))
o = list(product(a,b))
for i in o:
    print(i, end = ' ')
