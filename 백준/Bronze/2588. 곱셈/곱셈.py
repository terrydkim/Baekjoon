import sys

a,b = int(input()), sys.stdin.readline().rstrip()


for i in reversed(list(b)):
    print (a*int(i))
print(a*int(b))

