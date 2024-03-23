import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    l,r = map(int,input().split())
    arr.append((l-r,i))
    arr.append((l+r,i))

arr.sort()

answer = []
for i in arr:
    if answer:
        if answer[-1][1] == i[1]:
            answer.pop()
        else:
            answer.append(i)
    else:
        answer.append(i)

if answer:
    print("NO")

else:
    print("YES")

