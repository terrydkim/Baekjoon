import sys

a,b,c,d = map(int,sys.stdin.readline().split())

e = abs(a-c)
f = abs(b-d)

print(min(a,b,e,f))