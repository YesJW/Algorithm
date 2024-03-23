import sys

input = sys.stdin.readline

n = int(input())

dp = [[0] * 10 for _ in range(n)]
for i in range(0,10):
    dp[0][i] = 1
for i in range(1,n):
    for j in range(0,10):
        dp[i][j] += sum(dp[i-1][j:])

print(sum(dp[n-1]) % 10007)