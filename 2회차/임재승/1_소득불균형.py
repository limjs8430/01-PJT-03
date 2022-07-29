import sys

sys.stdin = open("_소득불균형.txt")

# 소득 불균형 D3

# 리스트로 소득을 받고
# 리스트의 합을 n번째 테스트 케이스의 숫자만큼 나누고
# 그 나눈 숫자보다 작을때마다 더해준다.



T = int(input())

for i in range(1, T+1):
    cnt = int(input())
    N = list(map(int, input().split()))
    rst = 0
    # print(sum(N)/(len(N)))
    # 그냥 리스트값의 평균 이하일때마다 출력할 값을 1씩 더해줬습니다.
    for n in N:
        if n <= sum(N)/cnt:
            rst += 1
        else:
            continue
    print(f'#{i} {rst}')