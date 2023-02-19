T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    max_sum = -999999
    for i in range(N - 1):
        sumation = lst[i] + lst[i + 1]  # 인접한 원소의 합 계산
        if max_sum < sumation:  # 최대값과 비교
            max_sum = sumation

    print(f'#{test_case} {max_sum}')