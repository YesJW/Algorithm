import sys
import time

input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

dp = [1e9] * (n)
dp[0] = 0
for i in range(len(arr)):
    if arr[i] == 0:
        continue
    for j in range(1,arr[i]+1):
        if i+j < n:
            dp[i+j] = min(dp[i+j], dp[i] + 1)
print(dp[-1] if dp[-1] != 1e9 else -1)