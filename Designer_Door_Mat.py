h,w = map(int, input().split())
for i in range(1, h, 2):
    print(str('.|.' * i).center(w, '-'))
print('WELCOME'.center(w, '-'))
for i in range(h-2, -1, -2):
    print(str('.|.' * i).center(w, '-'))
