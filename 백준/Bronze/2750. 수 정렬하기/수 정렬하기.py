import sys

a = int(input())

b = [int(sys.stdin.readline().strip()) for i in range(a)]

for i in range(len(b)-1):
    for j in range(len(b)-1,i,-1):
        if b[j-1] > b[j]:
            b[j-1],b[j] = b[j],b[j-1]


for i in b:
    print(i)