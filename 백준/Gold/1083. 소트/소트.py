import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))
s = int(input())
count = 0

for i in range(0,n):
    if s == 0:
        break

    if max(arr[i:i+s+1]) != arr[i]:
        ind = arr.index(max(arr[i:i+s+1]))
        s = s - (ind - i)
        arr = (arr[:i]+ [arr[ind]] + arr[i:])
        arr.pop(ind+1)

print(*arr)


