import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
def bfs():
    count = 0
    while q:
        x, y = q.popleft()
        for i in range(8):
            cx = x + dx[i]
            cy = y + dy[i]

            if n <= cx or cx < 0 or m <= cy or cy < 0:
                continue
            if mountain[cx][cy] > mountain[x][y]:
                count = 1
            if visit[cx][cy]:
                continue

            if mountain[cx][cy] == mountain[x][y]:
                q.append([cx,cy])
                visit[cx][cy] = True
    if count:
        return 0
    return 1

n, m = map(int,input().split())

mountain = [list(map(int, input().split())) for _ in range(n)]
q = deque()
visit = [[False] * m for _ in range(n)]
dx = [1,0,-1,0,1,-1,1,-1]
dy = [0,1,0,-1,1,1,-1,-1]
ans = 0
for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            q.append([i,j])
            visit[i][j] = True
            ans += bfs()
print(ans)