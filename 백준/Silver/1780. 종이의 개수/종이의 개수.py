import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n = int(input())

paper = [list(map(int,input().split())) for _ in range(n)]
answer = [0,0,0]

def check_paper(x,y, n):

    now = paper[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j] != now:
                d = n//3
                check_paper(x,y,d)
                check_paper(x, y+d, d)
                check_paper(x, y+2*d, d)
                check_paper(x + d, y, d)
                check_paper(x+d, y+d, d)
                check_paper(x+d, y+2*d, d)
                check_paper(x+2*d, y, d)
                check_paper(x+2*d, y+d, d)
                check_paper(x+2*d, y+2*d, d)
                return
    answer[now+1]+=1




check_paper(0,0,n)
print(answer[0])
print(answer[1])
print(answer[2])