import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(input().strip())

arr = list(set(arr))
arr.sort(key = len)

ans = []
ans.append(arr.pop())
while arr:
    h = arr.pop()
    l = len(h)
    for i in ans:
        if h in i[:l]:
            break
    else:
        ans.append(h)
print(len(ans))