import sys
import time

input = sys.stdin.readline

start = time.time()
n = int(input())
ans = 0
l = len(str(n))
if n >= 10:
    nine = 9
    for _ in range(l-2):
        nine = nine * 10 + 9
    while nine > 0:
        ans += (n - nine) * len(str(n))
        l -= 1
        n = nine
        nine //= 10

ans += n
print(ans)
