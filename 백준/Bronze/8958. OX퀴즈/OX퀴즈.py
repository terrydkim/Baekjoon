import sys

a = int(input())

for _ in range(a):

    b = list(sys.stdin.readline().strip())

    score = 0
    total = 0

    for i in range(len(b)):
        if b[i] == 'O':
            score += 1
            total += score
        else : score = 0
    print(total)
