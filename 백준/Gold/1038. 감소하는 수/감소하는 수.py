import sys
from itertools import combinations

n = int(sys.stdin.readline())

nums = []

for i in range(1,11):
    for j in combinations(range(10),i):
        combi = list(j)
        combi.sort(reverse=True)
        nums.append(int(''.join(map(str,combi))))
nums.sort()

if n >= len(nums):
    print(-1)
else:
    print(nums[n])
