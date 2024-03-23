import sys

input = sys.stdin.readline

n = int(input())

dp = [[1e9, []] for _ in range(n + 1)]
dp[1] = [0,[1]]
if n > 1:
    dp[2] = [1,[2,1]]
if n > 2:
    dp[3] = [1,[3,1]]

for i in range(4,n+1):
    dp[i][0] = min(dp[i][0],dp[i-1][0]+1)
    dp[i][1] = dp[i-1][1] + [i]
    if i % 2 == 0:
        dp[i][0] = min(dp[i][0], dp[i//2][0]+1)
        if len(dp[i//2][1] + [i]) < len(dp[i][1]):
            dp[i][1] = dp[i//2][1] + [i]
    if i % 3 == 0:
        dp[i][0] = min(dp[i][0], dp[i//3][0] + 1)
        if len(dp[i // 3][1] + [i]) < len(dp[i][1]):
            dp[i][1] = dp[i//3][1] + [i]
dp[-1][1].sort(reverse=True)
print(dp[-1][0])
print(*dp[-1][1])
