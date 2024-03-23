import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n = int(input())

step = input().strip()

dx = [-1,0,1,0]
dy = [0,1,0,-1]

now = 2
arr = [[0,0]]
for i in step:
    if i == 'R':
        now = (now + 1) % 4
    elif i == 'L':
        if now - 1 == -1:
            now = 3
        else:
            now -= 1
    else:
        arr.append([arr[-1][0]+dx[now], arr[-1][1]+dy[now]])

x_sort = sorted(arr,key=lambda x:x[0])
y_sort = sorted(arr,key=lambda x:x[1])
max_x, min_x = x_sort[-1][0], x_sort[0][0]
max_y, min_y = y_sort[-1][1], y_sort[0][1]

maze = [['#'] * (max_y - min_y+1) for _ in range(max_x - min_x+1)]
for i in arr:
    x = i[0] - min_x
    y = i[1] - min_y
    maze[x][y]='.'

for i in maze:
    print(''.join(i))