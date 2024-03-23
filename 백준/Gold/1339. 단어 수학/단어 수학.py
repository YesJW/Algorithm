import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
answer = 0
n = int(input())
arr = [list(input().strip()) for _ in range(n)]
alpha = {}

for word in arr:
    sq = len(word) - 1
    for i in range(len(word)):
        if word[i] not in alpha:
            alpha[word[i]] = 10 ** sq
        else:
            alpha[word[i]] += 10 ** sq
        sq -= 1

alpha = sorted(alpha.values(), reverse=True)
num = 9
for i in alpha:
    answer += i * num
    num -= 1
print(answer)