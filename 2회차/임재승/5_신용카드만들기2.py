import sys

sys.stdin = open("_신용카드만들기2.txt")

# 신용카드 만들기 2 D2

T = int(input())
# 가능한 시작자리 리스트
ok = ['3', '4', '5', '6', '9']

for i in range(1, T+1):
    credit = list(map(str, input()))
    # 크레딧에 -가 있으면 계속해서 remove를 해준다.
    while '-' in credit:
        credit.remove('-')
    # 우선 기본조건인 16자리가 아니면 0의 출력해주고
    # 그다음 완성되는 조건을 넣어준다.
    if len(credit) != 16:
        print(f'#{i} 0')
    elif credit[0] in ok:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')