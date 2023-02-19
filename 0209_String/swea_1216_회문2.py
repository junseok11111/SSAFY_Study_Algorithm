# import sys;sys.stdin=open('sample_input.txt', 'r')
def find_palindrome(arr, M):
    # 회문의 길이가 100개인 것부터 찾음
    # 없으면 회문의 길이를 하나씩 줄여감
    # i는 행, j는 열
    while M > 1:  # 패턴길이 M의 길이가 2 이상 까지만 반복
        for i in range(N):
            for j in range(N - M + 1):
                for k in range(M // 2):
                    if arr[i][j + k] != arr[i][j + M - 1 - k]:
                        break
                else:
                    return M  # 회문 찾으면 리턴

        # i는 열, j는 행
        for i in range(N):
            for j in range(N - M + 1):
                for k in range(M // 2):
                    if arr[j + k][i] != arr[j + M - 1 - k][i]:
                        break
                else:
                    return M  # 회문 찾으면 리턴
        M -= 1
    return 0


for _ in range(10):
    test_case = input()
    N = 100
    arr = [input() for _ in range(N)]

    print(f'#{test_case}', find_palindrome(arr, N))