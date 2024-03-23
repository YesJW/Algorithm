import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

fir = list(input().strip())
sec = list(input().strip())
len_fir = len(fir)
len_sec = len(sec)
dp = [[0] * (len_sec+1) for _ in range(len_fir+1)]

for i in range(1,len_fir+1):
    for j in range(1,len_sec+1):
        if fir[i-1] == sec[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])

