import sys
input = sys.stdin.readline

N = int(input())
N_num = list(map(int,input().split()))

M = int(input())
M_num = list(map(int,input().split()))

# 서칭해야되는 리스트 정렬
N_num.sort()

def search(lst,key):
    n = len(lst)
    pl = 0
    pr = n-1

    while pl <= pr:
        pc = (pl+pr)//2
        if key == lst[pc]:
            return 1 
        elif key > lst[pc]:
            pl = pc + 1
        else: pr = pc - 1
    return 0

for i in M_num:
    print(search(N_num, i))



