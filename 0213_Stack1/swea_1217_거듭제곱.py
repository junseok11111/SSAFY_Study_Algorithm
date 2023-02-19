def po(N, M):
    if M == 0:
        return 1
    M -= 1
    return N * po(N, M) # 재귀호출


for _ in range(10):
    test_case = input()
    N, M = map(int, input().split())
    print(f'#{test_case}', po(N, M))