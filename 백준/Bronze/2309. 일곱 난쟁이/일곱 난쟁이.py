# 아홉 난쟁이의 키 입력 받기
heights = [int(input()) for _ in range(9)]

# 아홉 난쟁이 중에서 일곱 난쟁이를 선택하는 모든 경우를 고려
for i in range(9):
    for j in range(i+1, 9):
        selected = heights[:i] + heights[i+1:j] + heights[j+1:]  # 선택된 일곱 명의 난쟁이들
        if sum(selected) == 100:  # 일곱 난쟁이의 키의 합이 100인 경우
            # 일곱 난쟁이의 키를 오름차순으로 출력
            for height in sorted(selected):
                print(height)
            exit()  # 출력 후 프로그램 종료
