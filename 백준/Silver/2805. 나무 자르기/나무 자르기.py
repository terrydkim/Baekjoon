import sys
input = sys.stdin.readline

N,M = map(int,input().split())

trees = list(map(int,input().split()))

def search(trees,m):
    left = 0
    right = max(trees)
    key = 0
    while left<=right :
        total = 0
        mid = (left+right)//2

        for tree in trees:
            if tree > mid:
                total += tree-mid

        if total < m:
            right = mid - 1
        else: 
            left = mid + 1
            key = mid
    return key

print(search(trees,M))