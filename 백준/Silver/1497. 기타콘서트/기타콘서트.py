import sys
from itertools import combinations


input = sys.stdin.readline

n, m = map(int, input().split())

guitar = [input().strip().split() for _ in range(n)]

count = 0
ans = -1
for i in range(1,len(guitar)+1):
    for j in combinations(guitar, i):
        num = 0
        for g, s in j:
            s = s.replace('Y', '1')
            s = s.replace('N', '0')
            num = (num | int(s,2))

        if num > count:
            count = num
            ans = i

print(ans)
