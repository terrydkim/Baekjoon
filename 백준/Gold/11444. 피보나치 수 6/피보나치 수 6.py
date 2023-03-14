import sys
input = sys.stdin.readline

N = int(input())

MOD = int(1e9) + 7

A = [[1, 1], [1, 0]]

def multiple(a,b):
    n = len(a)
    c = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
                c[i][j] %= MOD
    return c
def div(a,b):
    if b == 1:
        for i in range(len(a)):
            for j in range(len(a)):
                a[i][j] %= MOD
        return a
    else: 
        # 짝수면 
        if b % 2 == 0:
            temp = div(a,b//2)
            return multiple(temp, temp)
        #홀수면
        else :
            temp = div(a,b-1)
            return multiple(temp, a)

print(div(A,N)[0][1])

