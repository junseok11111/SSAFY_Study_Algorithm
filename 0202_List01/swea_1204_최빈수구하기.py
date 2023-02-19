# import sys;sys.stdin=open('input.txt', 'r')

# 학생 수 : 1000
# 학생 점수 0 <= score <= 100
for _ in range(int(input())):
    test_case = input()

    students = 1000
    A = list(map(int, input().split()))
    K = 100 # 자료의 최대값
    C = [0] * (K + 1)   # 공간은 K + 1개를 만듬 (마지막 index = K 여야함)

    # 1. 자료의 빈도수를 계산
    for val in A:
        C[val] += 1

    # 2. 빈도수 중 최대값과 해당 인덱스 찾기
    max_frequent, max_idx = 0, 0
    for idx in range(K + 1):
        if max_frequent <= C[idx]:
            max_frequent = C[idx]
            max_idx = idx

    # 3. 출력
    print(f'#{test_case} {max_idx}')