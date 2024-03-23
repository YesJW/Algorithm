import sys

input = sys.stdin.readline

a, b, n = map(int,input().split())
ans = 0
for _ in range(n):
    a = (a%b) * 10
    ans = a // b

print(ans)