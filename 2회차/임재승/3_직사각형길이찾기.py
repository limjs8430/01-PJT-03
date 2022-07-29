import sys

sys.stdin = open("_직사각형길이찾기.txt")

# 직사각형의 길이를 구한다
# 주어진 숫자 세개가 같으면 나머지도 같다
# 주어진 숫자중 두개는 같고 한개가 다르면 나머지는 다른 한개이다

T = int(input())

for i in range(1, T+1):
    x = list(map(int, input().split()))
    # 최대값의 카운터로 이용했는데
    # 3개 모두같으면 정사각형이므로 나머지도 같다.
    if x.count(max(x)) == 3:
        print(f'#{i} {max(x)}')
    # 2개만 같으면 남은 변의 길이와 같아야하므로 min을 출력
    elif x.count(max(x)) == 2:
        print(f'#{i} {min(x)}')
    else:
    # 모두 아니라면 max값 출력
        print(f'#{i} {max(x)}')


