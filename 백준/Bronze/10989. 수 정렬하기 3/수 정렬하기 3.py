import sys

n = int(sys.stdin.readline().rstrip())
nums = [0] * 10001  # 입력 받을 수 있는 범위(1~10,000)에 대한 리스트를 생성

for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    nums[num] += 1  # 입력받은 숫자를 nums 리스트에 추가하면서, 해당 숫자의 개수를 카운팅합니다.

for i in range(1, 10001):
    # 1~10000까지 반복하면서, 해당 숫자가 몇 개인지 출력합니다.
    # nums 리스트에는 각 숫자가 몇 개 있는지가 저장되어 있으므로, 그 개수만큼 반복해서 출력합니다.
    for j in range(nums[i]):
        print(i)
