import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    count = 0
    q = deque()

    q.append([x,y])

    while q:
        x, y = q.popleft()
        count+=1
        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y

            if 0<=cx<n and 0<=cy<m:
                if not visit[cx][cy] and arr[cx][cy]:
                    visit[cx][cy] = True

                    q.append([cx,cy])
    return count

n, m, k = map(int, input().split())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
answer = 0

arr = [[0] * m for _ in range(n)]
visit = [[False] * m for _ in range(n)]
for i in range(k):
    r, c = map(int, input().split())
    r-=1
    c-=1

    arr[r][c] = 1


for i in range(n):
    for j in range(m):
        if arr[i][j] and not visit[i][j]:
            visit[i][j] = True
            answer = max(answer, bfs(i,j))

print(answer)
