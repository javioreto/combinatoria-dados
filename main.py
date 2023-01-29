import random

combinatorias = {}

for n in range(100000):
    num = random.randint(1, 6) + random.randint(1, 6)
    if num in combinatorias:
        combinatorias[num] = combinatorias[num]+1
    else:
        combinatorias[num] = 1

combinatorias = dict(sorted(combinatorias.items(), key=lambda x:int(x[0])))

print(combinatorias)