import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))
arr = [0] + arr

dp = [0] * (n+1)

dp[1] = arr[1]

for i in range(2,n+1):
    for j in range(1,i):
        dp[i] = max(dp[i-j]+arr[j],arr[i], dp[i])
        if i % j == 0:
            dp[i] = max(dp[i], arr[j] * (i//j))

print(dp[-1])