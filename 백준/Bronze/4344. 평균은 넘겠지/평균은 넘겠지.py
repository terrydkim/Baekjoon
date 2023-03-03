import sys

a = int(input())

for i in range(a):
    b = list(map(int,sys.stdin.readline().split()))
    avg = sum(b[1:])/b[0]

    high = 0
    for i in b[1:]:
        if i > avg :
            high += 1
    per = (high/b[0])*100
    print(f'{per:.3f}%')
