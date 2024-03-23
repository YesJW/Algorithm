import sys
from collections import deque
from itertools import combinations

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

L, C = map(int, input().split())

arr = list(input().strip().split())
arr.sort()
answer = set()

for i2 in combinations(arr,L):
    if 'a' not in i2 and 'e' not in i2 and 'i' not in i2 and 'o' not in i2 and 'u' not in i2:
        continue
    s = ''.join(i2)
    a = s.count('a')
    e = s.count('e')
    i = s.count('i')
    o = s.count('o')
    u = s.count('u')
    s2 = a+e+i+o+u
    if len(s) - s2 <= 1:
        continue
    answer.add(''.join(sorted(i2)))
answer = sorted(list(answer))
for i in answer:
    print(i)