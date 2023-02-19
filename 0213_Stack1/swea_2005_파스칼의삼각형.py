T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    
    # 스택을 활용한 문제 해결
    S = [0] * N
    top = -1

    print(f'#{test_case}')
    for i in range(N):
        top += 1
        if top > 1:
            for t in range(top-1, 0, -1):
                S[t] = S[t] + S[t-1]        # 규칙성
        S[top] = 1
        print(*S[:top+1])