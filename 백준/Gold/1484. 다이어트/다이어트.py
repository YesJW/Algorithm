import sys
input = sys.stdin.readline

g = int(input())
left = 1
right = 1
ans = []
while left < g and right < g:

    tmp = (left + right) * (left - right)

    if tmp == g:
        ans.append(left)
    if tmp < g:
        left += 1
        continue
    right += 1

if not ans:
    print(-1)

else:
    for i in ans:
        print(i)
