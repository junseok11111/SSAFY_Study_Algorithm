def find_min(n, cal_sum):
    global min_val, N
    if min_val <= cal_sum:
        return

    if n == N:
        min_val = cal_sum
        return

    for col in range(n, N):
        p[n], p[col] = p[col], p[n]
        find_min(n+1, cal_sum + arr[n][p[n]])
        p[n], p[col] = p[col], p[n]


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = list(range(N))
    min_val = 10*N
    find_min(0, 0)
    print(f'#{test_case}', min_val)