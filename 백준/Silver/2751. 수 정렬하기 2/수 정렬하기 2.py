import sys
input = sys.stdin.readline

a = int(input())

b = [int(input().strip()) for _ in range(a)]

b.sort()

for i in b:
    print(i)