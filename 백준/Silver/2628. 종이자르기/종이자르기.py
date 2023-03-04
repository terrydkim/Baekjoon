import sys

x,y =  map(int,input().split())

X=[0,x]
Y=[0,y]

a= int(input())

for _ in range(a):
    xy,row = map(int,sys.stdin.readline().split())

    if xy == 0 :
        Y.append(row)
    else :
        X.append(row)
sort_X = X.sort()
sort_Y = Y.sort()

Max = 0
for i in range(len(X)-1):
    for j in range(len(Y)-1):
        width = X[i+1]-X[i]
        height = Y[j+1]-Y[j]
        Max = max(Max,width*height)

print(Max)