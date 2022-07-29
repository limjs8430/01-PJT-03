import sys

sys.stdin = open("_최빈수구하기.txt")

# 최빈수 구하기 D2

T = int(input())

for number in range(1, T+1):
    N = int(input())
    point = list(map(int, input().split()))
    # 0점부터 100점까지 받아줄 리스트
    # 위치에 있는 값이 곧 몇명인지 알려줍니다.
    list_point = [0] * 101
    for p in point:
        # 들어온 점수마다 1씩 증가
        list_point[p] += 1
    max_point = 0
    # 계속해서 최대값을 갱신 중복이여도 아래부터해서 높은게 출력
    for i in range(0, len(list_point)):
        if list_point[i] >= max_point:
            max_index = i
            max_point = list_point[i]
    print(f'#{number} {max_index}')