import sys

a = int(input())
b = list(map(int,sys.stdin.readline().split()))
c = 0

for i in b:
    d = 0
    if i == 1 :continue
    for j in range(2, i):
        if i % j == 0:
            d += 1
    if d == 0: c+=1

print(c)
