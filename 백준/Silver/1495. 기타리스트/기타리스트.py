import sys
from collections import deque

# 개수 N 시작볼륨 s 최대 볼륨 m
# 각 곡이 시작하기 전에 줄 수 있는 볼륨의 차이 + -

input = sys.stdin.readline

n, s, m = map(int, input().split())
v = list(map(int, input().split()))

dp = [[0] * (m+1) for _ in range(n+1)]

dp[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if dp[i][j] == 1:
            if j + v[i] <= m:
                dp[i+1][j + v[i]] = 1
            if j - v[i] >= 0:
                dp[i+1][j - v[i]] = 1

for i in range(m,-1,-1):
    if dp[n][i] == 1:
        print(i)
        break
else:
    print(-1)