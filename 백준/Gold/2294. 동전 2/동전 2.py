import sys

input = sys.stdin.readline

n, m = map(int,input().split())

money = [int(input()) for _ in range(n)]

dp = [1e9] * (m+1)
dp[0] = 0

for i in range(n):
    for j in range(money[i],m+1):
        dp[j] = min(dp[j], dp[j-money[i]] + 1)

if dp[-1] == 1e9:
    print(-1)
else:
    print(dp[-1])
