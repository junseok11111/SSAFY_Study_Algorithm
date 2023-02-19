T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    # 오른쪽과 아래쪽에 더미값 0 한줄 추가
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)]

    ans = 0
    for i in range(N+1):
        r_cnt = c_cnt = 0
        for j in range(N+1):
            # 가로 탐색
            if arr[i][j]:
                r_cnt += 1
            else:
                if r_cnt == K:
                    ans += 1
                r_cnt = 0   # 0이 나올 경우 count 초기화

            # 세로 탐색
            if arr[j][i]:
                c_cnt += 1
            else:
                if c_cnt == K:
                    ans += 1
                c_cnt = 0   # 0이 나올 경우 count 초기화
    print(f'#{test_case}', ans)