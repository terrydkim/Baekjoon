import sys

a = int(input())

for _ in range(a):
    b = list(sys.stdin.readline().strip())
    for i in range(2,len(b)):
        print(int(b[0])*b[i], end="")
    print()