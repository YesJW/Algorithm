import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

t = int(input())


def max_score():
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if n == 1:
        print(max(arr[0][0], arr[1][0]))
        return
    dp[0][1] = arr[1][0] + arr[0][1]
    dp[1][1] = arr[0][0] + arr[1][1]

    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        return
    for i in range(2,n):
        dp[0][i] = max(dp[1][i-2] + arr[0][i], dp[1][i-1]+arr[0][i])
        dp[1][i] = max(dp[0][i - 2] + arr[1][i], dp[0][i - 1] + arr[1][i])
    print(max(dp[0][-1],dp[1][-1]))

for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    max_score()
