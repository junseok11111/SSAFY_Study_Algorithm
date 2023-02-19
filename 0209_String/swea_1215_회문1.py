def find_palindrome(arr, N):
    cnt = 0
    # 가로행에서 회문 찾기
    for i in range(8):
        for j in range(8 - N + 1):
            for k in range(N//2):                   # 회문의 중간 지점을 활용
                if arr[i][j+k] != arr[i][j+N-1-k]:  # 중간지점에 대칭되는 지점의 값들을 비교
                    break
            else:
                cnt += 1                            # 찾으면 카운팅
    
    # 세로열에서 회문 찾기
    for i in range(8):
        for j in range(8 - N + 1):
            for k in range(N//2):
                if arr[j+k][i] != arr[j+N-1-k][i]:
                    break
            else:
                cnt += 1
    return cnt


for test_case in range(1, 11):
    N = int(input())                    # 찾아야 하는 회문의 길이
    arr = [input() for _ in range(8)]
    print(f'#{test_case}', find_palindrome(arr, N))