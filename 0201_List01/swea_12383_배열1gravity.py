T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 가로의 길이
    lst = list(map(int, input().split()))

    max_cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if lst[i] > lst[j]: # lst[i]보다 작은 값을 가진 경우
                cnt += 1        # 낙차 +1
        if max_cnt < cnt:       # 최대 낙차수와 비교
            max_cnt = cnt


    print(f'#{test_case} {max_cnt}')