import sys

a = int(sys.stdin.readline())

b = a % 4 == 0
c = a % 100 != 0
d = a % 400 == 0

if b and( c or d):
    print(1)
else : print(0)
