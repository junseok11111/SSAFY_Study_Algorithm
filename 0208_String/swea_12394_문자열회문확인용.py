import sys;sys.stdin=open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    matrix = [list(input()) for _ in range(N)]

    a = 0 if M % 2 else 1
    d = M // 2

    result = ''
    for i in range(N):
        for j in range(d, N - d + 1):

            # 가로행 찾기
            r_word = '' if a else matrix[i][j]
            for m in range(1, d + 1):
                r_word = matrix[i][j-m] + r_word + matrix[i][j+m-a]
                if matrix[i][j-m] != matrix[i][j+m-a]:
                    break
            else:
                result = r_word
                break

            # 세로열 찾기
            c_word = '' if a else matrix[j][i]
            for m in range(1, d + 1):
                c_word = matrix[j-m][i] + c_word + matrix[j+m-a][i]
                if matrix[j-m][i] != matrix[j+m-a][i]:
                    break
            else:
                result = c_word
                break

        if result:
            break

    print(f'#{test_case}', result)