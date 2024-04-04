import sys

input = sys.stdin.readline

n, m = map(int,input().split())
k = set(input().split()[1:])
party = []
answer = m

for _ in range(m):
    party.append(set(input().split()[1:]))

for _ in range(m):
    for p in party:
        if p & k:
            k = k.union(p)

for p in party:
    if p & k:
        answer-=1
print(answer)