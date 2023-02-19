for test_case in range(1, int(input()) + 1):
    N = int(input())
    C = list(map(int, input().split()))

    max_cnt, cnt = 1, 1
    for i in range(1, N):
        if C[i] - C[i-1] == 1:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 1

    print(f'#{test_case} {max_cnt}')

