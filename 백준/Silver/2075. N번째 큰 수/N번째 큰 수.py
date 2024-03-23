import heapq
import sys
from collections import deque
from heapq import heappop,heappush

input = sys.stdin.readline

n = int(input())

heap = []

for i in range(n):
    num = list(map(int,input().split()))
    for j in num:
        if len(heap) < n:
            heappush(heap, j)
        else:
            if heap[0] < j:
                heappop(heap)
                heappush(heap,j)
print(heappop(heap))
