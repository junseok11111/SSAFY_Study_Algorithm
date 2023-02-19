T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_total = 0
    for row in range(N-M+1):
        for col in range(N-M+1):
            total = 0
            for rm in range(M):
                for cm in range(M):
                    total += matrix[row+rm][col+cm]
            if max_total < total:
                max_total = total

    print(f'#{test_case}', max_total)