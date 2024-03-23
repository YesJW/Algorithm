import heapq
import sys
from collections import deque
from heapq import heappop,heappush

input = sys.stdin.readline

n, m = map(int,input().split())

arr = [list(map(str, input().strip())) for _ in range(n)]
min_line = min(n,m)
max_line = max(n,m)
ans = 0
for i in range(min_line,0,-1):
    for x in range(n):
        for y in range(m):
            if x + i >= n or y + i >= m:
                continue
            if arr[x][y] == arr[x+i][y] == arr[x][y+i] == arr[x+i][y+i]:
                print((i+1)**2)
                sys.exit()
else:
    print(1)