import sys
from collections import deque
input = sys.stdin.readline

r, c, k = map(int, input().split())

arr = [list(input().strip()) for _ in range(r)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

visit = [[False] * c for _ in range(r)]

visit[r-1][0] = True
global ans
ans = 0
def dfs(x, y, count):
    if x == 0 and y == c-1:
        if count == k:
            global ans
            ans+=1
        return
    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]

        if 0<=cx<r and 0 <= cy < c:
            if not visit[cx][cy] and arr[cx][cy] == '.':
                visit[cx][cy] = True
                dfs(cx,cy,count+1)
                visit[cx][cy] = False


dfs(r-1,0,1)
print(ans)