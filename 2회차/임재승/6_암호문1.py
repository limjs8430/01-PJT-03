import sys

sys.stdin = open("_암호문1.txt")

# len_ = 암호문의 길이
# ori_ = 원본 암호문
# test_number = 명령어의 갯수
# testing = 명령어


for test_case in range(1, 11):
    len_ = int(input())
    ori = list(map(int, input().split()))
    test_number = int(input())
    testing = list(map(str, input().split()))

    for i in range(len(testing)):
        # I가 나오면
        if testing[i] == 'I':
            # I가 나온 다음 번호의 위치에 값을 넣어줘야해서 
            # 그 값이 들어가는 변수를 지정
            where = int(testing[i+1])
            # i, i+1(값이 들어가는 위치), i+2(몇개가 들어가는지)
            # i + 3 부터 i + 2 까지
            for j in range(i + 3 , i + 3 + int(testing[i+2])):
                ori.insert(where, int(testing[j]))
                where += 1
    # 컴프리 핸션을 사용해 출력
    print(f'#{test_case} {" ".join(map(str, ori[:10]))}')