import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
x, y, now = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
#위 오른 아래 왼
dx = [-1,0,1,0]
dy = [0,1,0,-1]

q = deque()
q.append([x,y])
visit[x][y] = True
ans = 1
while q:
    x, y = q.popleft()
    for _ in range(4):
        now = (now+3) % 4

        cx = x + dx[now]
        cy = y + dy[now]
        if cx < 0 or cx >= n or cy < 0 or m <= cy:
            continue
        if not visit[cx][cy] and room[cx][cy] == 0:
            q.append([cx,cy])
            visit[cx][cy] = True
            ans += 1
            break
    else:
        dir = now - 2
        cx = x + dx[dir]
        cy = y + dy[dir]
        if cx < 0 or cx >= n or cy < 0 or m <= cy:
            break
        if room[cx][cy] == 1:
            break

        q.append([cx,cy])


print(ans)

