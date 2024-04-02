import sys
from collections import deque
input = sys.stdin.readline

a, b, c = map(int, input().split())

q = deque()

x, y = 0, 0

q.append([0, 0])
ans = []
visit = [[False] * (b+1) for _ in range(a+1)]
visit[0][0] = True

def check(a, b):
    if not visit[a][b]:
        visit[a][b] = True
        q.append([a,b])

while q:
    x, y = q.popleft()

    z = c-x-y

    if x == 0:
       ans.append(z)

    # a -> b
    tmp = min(x, b-y)
    check(x-tmp, y+tmp)

    # a -> c
    tmp = min(x, c-z)
    check(x-tmp, y)

    # b -> a
    tmp = min(a-x, y)
    check(x+tmp, y-tmp)

    # b -> c
    tmp = min(y, c-z)
    check(x, y-tmp)

    # c -> a
    tmp = min(z, a-x)
    check(x+tmp, y)

    # c -> b
    tmp = min(z, b-y)
    check(x, y+tmp)

print(*(sorted(ans)))