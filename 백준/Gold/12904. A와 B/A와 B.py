import sys
from collections import deque
input = sys.stdin.readline

#문자열 뒤에 A 추가 or 문자열 뒤집고 B 추가
#가능하면 1 아니면 0


s = input().strip()
t = input().strip()


arr = deque()
arr.append(s)

for i in range(len(t)):
    if t[-1] == 'A':
        t = t[:-1]
    elif t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]
    if s == t:
        print(1)
        break
else:
    print(0)