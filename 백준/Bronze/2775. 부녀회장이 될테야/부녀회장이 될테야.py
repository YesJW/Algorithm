from itertools import product
import sys

input = sys.stdin.readline


#k층 n호
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    dp = [[i for i in range(1, 15)] for _ in range(k+1)]
    for i in range(1,k+1):
        for j in range(1,14):
            dp[i][j] = dp[i][j-1]+dp[i-1][j]
    print(dp[k][n-1])

