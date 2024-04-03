import sys

input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))

# + - * %
op = list(map(int, input().split()))

minimum = 1e9
maximum = -1e9


def dfs(depth, p, m, mul, div, total):
    global minimum
    global maximum
    if depth == n:
        minimum = min(total, minimum)
        maximum = max(total, maximum)
        return

    if p:
        dfs(depth + 1, p - 1, m, mul, div, total + number[depth])
    if m:
        dfs(depth + 1, p, m - 1, mul, div, total - number[depth])
    if mul:
        dfs(depth + 1, p, m, mul - 1, div, total * number[depth])
    if div:
        dfs(depth + 1, p, m, mul, div - 1, int(total / number[depth]))


dfs(1, op[0], op[1], op[2], op[3], number[0])
print(maximum)
print(minimum)
