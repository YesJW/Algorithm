import sys

input = sys.stdin.readline

n = int(input())

student = list(map(int, input().split()))

stack = []

now_number = 1

for s in student:
    stack.append(s)

    while stack and stack[-1] == now_number:
        stack.pop()
        now_number+=1

if stack:
    print("Sad")
else:
    print("Nice")
