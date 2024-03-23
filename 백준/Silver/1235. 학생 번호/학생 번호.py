import sys

input = sys.stdin.readline

n = int(input())

student = [input().strip() for _ in range(n)]

for i in range(1,len(student[0])+1):
    a = set()
    for j in student:
        a.add(j[-i:])
    if len(a) == n:
        print(i)
        break
