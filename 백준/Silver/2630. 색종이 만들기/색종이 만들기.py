import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]

answer = [0,0]
def count_paper(x,y,n):
    color = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j] != color:
                d = n//2
                count_paper(x,y,d)
                count_paper(x,y+d,d)
                count_paper(x+d, y, d)
                count_paper(x+d, y + d, d)
                return
    answer[color] += 1
count_paper(0,0,n)
print(answer[0])
print(answer[1])
