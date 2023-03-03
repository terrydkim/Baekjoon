import sys

a = [int(sys.stdin.readline().strip()) for _ in range(9)]

b = max(a)
print(b, a.index(b)+1, sep='\n')


