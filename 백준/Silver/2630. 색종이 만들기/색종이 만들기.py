import sys
input = sys.stdin.readline

N = int(input())

papers = [list(map(int, input().strip().split())) for _ in range(N)]

# print(papers)
white, blue = 0,0


def cut(x, y, n):
    global white, blue
    color = papers[x][y]
    for j in range(x, x+n):
        for i in range(y, y+n):
            # 왼쪽 위 컬러랑 다르면 자르기
            if color != papers[j][i]:
                # 1사분면
                cut(x, y, n//2)
                # 2사분면
                cut(x, y+n//2, n//2)
                # 3사분면
                cut(x+n//2, y, n//2)
                # 4사분면
                cut(x+n//2, y+n//2, n//2)
                # 재귀 스택 막기
                return
    if color == 0:
        white += 1
    else:
        blue += 1

cut(0,0,N)
print(white,blue,sep='\n')
