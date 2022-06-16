from collections import Counter
num_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
num_customers = int(input())
shoes_demand = list(map(tuple, (map(int,input().split()) for _ in range(num_customers))))
u_shoe_sizes = Counter(shoe_sizes)
money = 0
for one_shoe_size in shoes_demand:
    if one_shoe_size[0] in u_shoe_sizes.keys() and u_shoe_sizes[one_shoe_size[0]] >0 :
        u_shoe_sizes[one_shoe_size[0]] = u_shoe_sizes[one_shoe_size[0]]-1
        money = money+one_shoe_size[1]
          
print(money)
