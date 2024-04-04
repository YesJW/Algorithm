import copy
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

lab = [list(map(int,input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
ans = 0
def bfs():
    global ans
    q = deque()
    lab_copy = copy.deepcopy(lab)

    for i in range(n):
        for j in range(m):
            if lab_copy[i][j] == 2:
                q.append([i,j])

    while q:
        x,y = q.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]

            if 0<=cx<n and 0<=cy<m and lab_copy[cx][cy] == 0:
                lab_copy[cx][cy] = 2
                q.append([cx,cy])

    count = 0
    for i in lab_copy:

        count += i.count(0)
    ans = max(ans, count)




def wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall(count+1)
                lab[i][j] = 0

wall(0)
print(ans)