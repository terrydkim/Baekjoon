import sys

a = int(input())

for _ in range(a):
    b,c = sys.stdin.readline().strip().split()
    for i in c:
        print(i*int(b), end='')
    print()