import sys
from collections import deque
import time
input = sys.stdin.readline

n = int(input())

arr = [i for i in range(1,n+1)]
arr = deque(arr)
for i in range(n-1):
    arr.popleft()
    arr.append(arr.popleft())
print(*arr)
