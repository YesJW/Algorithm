import sys
from collections import deque

# 개수 N 나무 자르는 비용 C 값 W

input = sys.stdin.readline

n, c, w = map(int,input().split())

tree = [int(input()) for _ in range(n)]
tree.sort()

ans = 0

for i in range(1,tree[n-1]+1):
    money = 0
    for j in range(n):
        count_t, remain = divmod(tree[j],i)
        cost = tree[j] // i * c
        if tree[j] % i == 0:
            cost -= c
        if count_t * w * i - cost < 0:
            continue
        money += count_t * w * i - cost

    ans = max(ans, money)

print(ans)
