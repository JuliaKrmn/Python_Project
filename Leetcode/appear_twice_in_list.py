from collections import defaultdict

a = [-1, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 1, 2, -1, -4]
seen = defaultdict(int)
result = []

for num in a:
    if seen[num] < 2:
        result.append(num)
        seen[num] += 1

print(result)