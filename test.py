from itertools import permutations

a = [1, 2, 3, 4, 5]
for i, j in permutations(a, 2):
    print(i)
