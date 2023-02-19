import sys;sys.stdin=open('sample_input.txt', 'r')

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]

    ans = 0
    for r in range(N):
        i = j = k = 0   # i는 문자열 처음부터, j는 문자열 마지막부터, k는 문자열 기준점
        while k + M <= N:
            if matrix[r][i] != matrix[r][k + j+(M-1)]:
                i = i + j + 1
                j = 0
                k = i
            else:
                i += 1
                j -= 1

            if i == k + M//2:
                ans = 1
                print(f'#{test_case}', end=' ')
                for m in range(M):
                    print(matrix[r][k+m], end='')
                print()
                break
        if ans:
            break
    else:
        for c in range(N):
            i = j = k = 0  # i는 문자열 처음부터, j는 문자열 마지막부터, k는 문자열 기준점
            while k + M <= N:
                if matrix[i][c] != matrix[k + j + (M - 1)][c]:
                    i = i + j + 1
                    j = 0
                    k = i
                else:
                    i += 1
                    j -= 1

                if i == k + M // 2:
                    ans = 1
                    print(f'#{test_case}', end=' ')
                    for m in range(M):
                        print(matrix[k + m][c], end='')
                    print()
                    break
            if ans:
                break