import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

visit = [[False] * n for _ in range(n)]
dp[0][0] = 1
visit[0][0] = True

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        next = arr[i][j]


        if i + next < n and j < n and visit[i][j]:
            dp[i+next][j] += dp[i][j]
            visit[i+next][j] = True

        if i < n and j + next < n and visit[i][j]:
            dp[i][j+next] += dp[i][j]
            visit[i][j + next] = True
print(dp[-1][-1])
