T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # 2 <= M < N

    arr = list(map(int, input().split()))

    max_sum, min_sum = -999999, 999999

    for i in range(N - M + 1):
        s = 0
        for j in range(i, i + M):   # 구간마다 합 계산 반복
            s += arr[j]

        if max_sum < s:
            max_sum = s

        if min_sum > s:
            min_sum = s

    print(f'#{test_case} {max_sum - min_sum}')


"""
#윈도우 슬라이딩 방식

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # 2 <= M < N
    a = list(map(int, input().split()))

    for idx in range(1, N):         # 누적합 계산
        a[idx] = a[idx-1] + a[idx]

    max_sum = min_sum = a[M-1]      # 최대,최소값 초기값 설정

    for i in range(M, N):
        val = a[i] - a[i - M]       # 누적합을 활용하여 구간의 합을 얻음
        if max_sum < val:
            max_sum = val

        if min_sum > val:
            min_sum = val

    print(f'#{test_case} {max_sum - min_sum}')

"""