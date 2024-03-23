n = int(input())
m = int(input())
btn = []
if m > 0:
    btn = list(map(int, input().split()))
answer = abs(100-n)

for i in range(1000001):
    for j in str(i):
        if int(j) in btn:
            break
    else:
        answer = min(answer, len(str(i))+ abs(i-n))

print(answer)