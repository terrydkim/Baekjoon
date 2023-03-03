import sys

# A = int(input())
A = int(sys.stdin.readline())
x = 0
if 100 > A :
    x = A
    print(x)
else:
    x = 99
    for i in range(111,A+1):
        a = list(map(int,str(i)))
        if a[0]-a[1] == a[1]-a[2]:
            x += 1
    print(x)
