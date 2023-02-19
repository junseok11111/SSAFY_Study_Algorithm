def func(i, cal_sum):
    global K, cnt
    if cal_sum == K:
        cnt += 1
        return
    if cal_sum > K:return
    if i == N:return

    else:
        func(i+1, cal_sum+A[i])
        func(i+1, cal_sum)


T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    func(0, 0)
    print(f'#{test_case}', cnt)