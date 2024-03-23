import sys
input = sys.stdin.readline

arr = [999999999] * 1001
arr[0] = 0
c, n = map(int, input().split())

cost = []
for i in range(n):
    cost.append(list(map(int,input().split())))

cost.sort(key= lambda x: (x[0]))

for i in range(1,cost[0][1]+1):
    arr[i] = cost[0][0]

for i in range(1,1001):
    for j in cost:
        c2 = i-j[1]
        if c2 < 0:
            c2 = 0
        arr[i] = min(arr[i], arr[c2] + j[0])

print(arr[c])