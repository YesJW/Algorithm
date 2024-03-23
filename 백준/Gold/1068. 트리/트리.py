def dfs(num, arr):
    arr[num] = -9
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)


n = int(input())

arr = list(map(int, input().split()))

d = int(input())

dfs(d ,arr)

answer = 0
for i in range(len(arr)):
    if i not in arr and arr[i] != -9:
        answer += 1
print(answer)
