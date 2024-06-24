import sys
from itertools import combinations
input = sys.stdin.readline

#신맛은 곱 쓴맛은 합 신 = S 쓴 = B
n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
combi = [combinations(arr, i) for i in range(1, n+1)]
answer = 1e9
for i in combi:
    for j in i:
        S, B = 1, 0
        for s, b in j:
            S *= s
            B += b
        answer = min(answer, abs(S-B))
print(answer)