# 아홉 난쟁이의 키 입력 받기
heights = [int(input()) for _ in range(9)]

# 일곱 난쟁이의 키를 저장할 리스트
selected = [0] * 7

# 아홉 난쟁이 중에서 일곱 난쟁이의 키를 선택하는 함수
def find_seven_dwarfs(cnt, start, total):
    if cnt == 7:  # 일곱 명의 난쟁이를 모두 선택한 경우
        if total == 100:  # 선택한 난쟁이들의 키의 합이 100인 경우
            # 일곱 난쟁이의 키를 오름차순으로 출력
            for height in sorted(selected):
                print(height)
            exit()  # 출력 후 프로그램 종료
        return
    for i in range(start, 9):
        selected[cnt] = heights[i]  # 현재 인덱스의 난쟁이를 선택
        find_seven_dwarfs(cnt+1, i+1, total+heights[i])  # 다음 인덱스를 선택하기 위해 재귀 호출
        selected[cnt] = 0  # 선택한 난쟁이를 다시 초기화

find_seven_dwarfs(0, 0, 0)  # 함수 호출
