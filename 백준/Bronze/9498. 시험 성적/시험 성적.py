import sys

a = int(sys.stdin.readline())

if 90 <= a <= 100 :
    print('A')
elif 80 <= a <90:
    print("B")
elif 70 <= a <80:
    print("C")
elif 60 <= a <70:
    print("D")
else : print('F')