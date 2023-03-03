a,b,c = map(int,input().split())

day = (c-b)/(a-b)
d = int(day) if day == int(day) else int(day)+1
print(d)