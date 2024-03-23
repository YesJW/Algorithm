import sys
input = sys.stdin.readline


time = 0

n = int(input())

w = list(map(int,input().split()))

m = int(input())
m_w = list(map(int, input().split()))


w.sort(reverse=True)
m_w.sort(reverse= True)

while m_w:
    w_c = w.copy()
    if m_w[0] > w_c[0]:
        break

    ind = 0
    while w_c:
        if m_w[ind] <= w_c[0]:
            w_c = w_c[1:]
            m_w = m_w[:ind] + m_w[ind+1:]
        else:
            ind+=1
        if ind >= len(m_w):
            break

    time+=1

if time == 0:
    print(-1)
else: print(time)