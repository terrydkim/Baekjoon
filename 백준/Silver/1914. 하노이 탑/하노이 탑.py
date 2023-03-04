import sys

a = int(sys.stdin.readline())

# x는 시작기둥 ,y는 목표기둥
def move(n, x, y):

    if n > 1:
        move(n-1, x, 6-x-y)

    print(x,y,sep=' ')
    if n > 1:
        move(n-1, 6-x-y, y)


print(2**a-1)
if a <= 20:
    move(a, 1, 3)