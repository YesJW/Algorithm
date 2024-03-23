import sys
import time

input = sys.stdin.readline

n, k = map(int,input().split())

arr = [1] * (n+1)
count = 0
for i in range(2,n+1):
    for j in range(1,n+1):
        if i * j <= n and arr[i*j]:
            arr[i*j] = 0
            count += 1
            if count == k:
                print(i*j)
                sys.exit()
