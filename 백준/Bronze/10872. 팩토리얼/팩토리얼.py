import sys

a = int(sys.stdin.readline())

def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1


print(factorial(a))