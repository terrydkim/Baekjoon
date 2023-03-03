
import sys  
n = int(input())

for _ in range (n):
    a = list(map(int, sys.stdin.readline().split()))
    print(sum(a))
