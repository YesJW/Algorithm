import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

money = int(input())

arr.sort()

if sum(arr) <= money:
    print(max(arr))
    sys.exit()

s = 0
e = max(arr)

while s <= e:
    mid = (s+e) // 2
    total = 0
    for i in arr:
        if i > mid:
            total += mid
        else:
            total += i

    if total > money:
        e = mid-1
    else:
        s = mid+1
print(e)
