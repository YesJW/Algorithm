import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

candy = [list(input().strip()) for _ in range(n)]

def check():
    ans = 1
    for i in range(n):
        count = 1
        for j in range(1,n):
            if candy[i][j] == candy[i][j-1]:
                count+=1
                ans = max(count, ans)
            else:
                count = 1
        count = 1
        for j in range(1,n):
            if candy[j][i] == candy[j-1][i]:
                count+=1
                ans = max(count,ans)
            else:
                count = 1
    return ans

answer = 0
for i in range(n):
    for j in range(n):

        if i + 1 < n:
            if candy[i][j] != candy[i+1][j]:
                candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
                ans = check()
                candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
                answer = max(ans, answer)

        if j + 1 < n:
            if candy[i][j] != candy[i][j+1]:
                candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
                ans = check()
                candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
                answer = max(ans, answer)
print(answer)