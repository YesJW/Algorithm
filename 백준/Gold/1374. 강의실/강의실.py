import sys
import heapq

input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[1])
classroom = []
ans = 0
for num,s,e in arr:
    while classroom and classroom[0] <= s:
        heapq.heappop(classroom)
    heapq.heappush(classroom,e)
    ans = max(ans, len(classroom))


print(ans)
