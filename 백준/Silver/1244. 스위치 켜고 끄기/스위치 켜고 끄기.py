import sys
input = sys.stdin.readline

n = int(input())

switch = [0] + list(map(int, input().split()))

student = int(input())

for i in range(student):

    s, number = map(int, input().split())
    if s == 1:
        d = (len(switch)-1) // number
        for j in range(1, d+1):
            if not switch[j * number]:
                switch[j * number] = 1
                continue
            switch[j * number] = 0
        continue
    if switch[number]:
        switch[number] = 0
    else:
        switch[number] = 1

    for j in range(1, len(switch)):
        if number - j < 1 or number + j >= len(switch):
            break
        if switch[number - j] == switch[number + j]:
            if switch[number-j]:
                switch[number - j] = 0
                switch[number + j] = 0
            else:
                switch[number-j] = 1
                switch[number+j] = 1
        else:
            break

for i in range(1,len(switch)):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()
