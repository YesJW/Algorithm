import sys
from collections import deque
from math import factorial
input = sys.stdin.readline

n = int(input())

balloon = list(map(int,input().split()))

q = deque()

for i, j in enumerate(balloon):
    q.append([i,j])


ind = 1
ans = []
while q:
    ind, num = q.popleft()
    ans.append(ind+1)
    if q:
        if num < 0:
            for _ in range(abs(num)):
                q.appendleft(q.pop())
        else:
            for _ in range(num-1):
                q.append(q.popleft())

print(*ans)