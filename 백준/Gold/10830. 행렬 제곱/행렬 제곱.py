def multiply_matrix(a, b):
    n = len(a)
    c = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
                c[i][j] %= 1000
    return c


def divide_matrix(a, b):
    if b == 1:
        for i in range(len(a)):
            for j in range(len(a)):
                a[i][j] %= 1000
        return a
    elif b % 2 == 0:
        temp = divide_matrix(a, b//2)
        return multiply_matrix(temp, temp)
    else:
        temp = divide_matrix(a, b-1)
        return multiply_matrix(temp, a)


n, b = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

result = divide_matrix(a, b)
for row in result:
    print(' '.join(map(str, row)))
