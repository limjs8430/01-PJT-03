import sys

sys.stdin = open("_신용카드만들기1.txt")

# 신용카드 만들기 1 D2

T = int(input())


for i in range(1, T+1):
    credit = list(map(int, input().split()))
    credit_sum = 0
    # 신용카드 룬 공식
    for number in range(0, len(credit)):
        if number % 2 == 0:
            credit_sum += 2*(credit[number])
        else:
            credit_sum += credit[number]
    print(f'#{i} {(10- (credit_sum%10))%10}')