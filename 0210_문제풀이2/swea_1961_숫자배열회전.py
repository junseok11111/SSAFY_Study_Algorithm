def join_lst(lst):
    result = ''
    for val in lst:result += val
    return result

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    spin_90 = [[arr[j][i] for j in range(N-1, -1, -1)] for i in range(N)]
    spin_180 = [[arr[i][j] for j in range(N-1, -1, -1)] for i in range(N-1, -1, -1)]
    spin_270 = [[arr[j][i] for j in range(N)] for i in range(N-1, -1, -1)]

    print(f'#{test_case}')
    for i in range(N):
        print(join_lst(spin_90[i]), join_lst(spin_180[i]), join_lst(spin_270[i]))