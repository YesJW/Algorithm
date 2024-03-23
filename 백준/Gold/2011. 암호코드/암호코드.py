import sys
import time

input = sys.stdin.readline

n = list(map(int,input().strip()))

dp = [0] * (len(n)+1)
dp[0] = 1
dp[1] = 1
if n[0] == 0:
    print(0)
else:
    n = [0] + n
    for i in range(2,len(n)):
        if n[i] != 0:
            dp[i] += dp[i-1]

        if 10 <= n[i-1] * 10 + n[i] <= 26:
            dp[i] += dp[i-2]
    print(dp[-1] % 1000000)