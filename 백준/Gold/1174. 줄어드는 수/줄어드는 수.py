import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(1,11):
    for j in combinations(range(0,10),i):
        j = list(j)
        j.sort(reverse=True)
        arr.append(int(''.join(map(str,j))))
arr.sort()
if n > len(arr):
    print(-1)
else:
    print(arr[n-1])
