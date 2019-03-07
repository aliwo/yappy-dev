import collections

list = [4, 6, 2, 2, 6, 4, 4, 4 ]
result = []

counter = collections.Counter(list)
for i in counter.keys():
    for j in range(counter[i]):
        result.append(i)

print(result)
