import math
import sys
from itertools import combinations
from collections import deque
from math import factorial

input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

dp[1] = 1

for i in range(2,n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[-1])