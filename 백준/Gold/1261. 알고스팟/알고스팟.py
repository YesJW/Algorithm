import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int,input().split())

maze = [list(input().strip()) for _ in range(m)]
dist = [[-1] * n for _ in range(m)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

queue = deque()
queue.append([0,0])
dist[0][0] = 0
while queue:
    x, y = queue.popleft()
    for i in range(4):
        mx, my = x+dx[i], y+dy[i]
        if 0 > mx or mx >= n or 0 > my or my >= m:
            continue
        if dist[my][mx] == -1:
            if maze[my][mx] == '0':
                dist[my][mx] = dist[y][x]
                queue.appendleft([mx,my])
            else:
                dist[my][mx] = dist[y][x] + 1
                queue.append([mx,my])
print(dist[m-1][n-1])