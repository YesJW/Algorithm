import sys

input = sys.stdin.readline

n = int(input())

student = list(map(int, input().split()))

stack = []

now_number = 1

while True:
    if stack and not student and stack[-1] != now_number:
        print("Sad")
        break
    if now_number == n+1:
        print("Nice")
        break
    if student and student[0] == now_number:
        student.pop(0)
        now_number+=1
        continue
    if stack and stack[-1] == now_number:
        stack.pop()
        now_number+=1
        continue
    if student:
        stack.append(student.pop(0))
