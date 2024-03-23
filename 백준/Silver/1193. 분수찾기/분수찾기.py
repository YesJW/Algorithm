import heapq
import sys
from collections import deque
from heapq import heappop,heappush

input = sys.stdin.readline

n = int(input())

line = 1

while line < n:
    n -= line
    line+=1
if line % 2 == 0:
    a = n
    b = line - n + 1
else:
    a = line - n + 1
    b = n
print(f'{a}/{b}')