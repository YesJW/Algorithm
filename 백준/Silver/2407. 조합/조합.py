import sys
from collections import deque
from math import factorial
input = sys.stdin.readline

n, m = map(int,input().split())

print(factorial(n)//(factorial(m) * factorial(n-m)))