import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
s = []
for i in combinations(arr,m):
    if i not in s:
        s.append(i)

for i in s:
    print(*i)