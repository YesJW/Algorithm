import sys
input = sys.stdin.readline

n = int(input())
lope = [int(input()) for _ in range(n)]

lope.sort(reverse=True)

ans = 0

for i in range(n):
    if ans <= lope[i] * (i+1):
        ans = max(ans,lope[i] * (i+1))
print(ans)
