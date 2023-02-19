def DFS(r, c):
    arr[r][c] = 1
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if arr[nr][nc] == 0:
            if DFS(nr, nc):     # DFS(nr, nc)의 리턴값이 1인 경우
                return 1        # 리턴 1
        elif arr[nr][nc] == 3:  # 인접한 곳이 3일경우 리턴 1
            return 1
    return 0


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [[1]*(N+2)] + [[1]+list(map(int, list(input())))+[1] for _ in range(N)] + [[1]*(N+2)]

    for row in range(1, N+1):
        if 2 in arr[row]:
            col = arr[row].index(2)
            print(f'#{test_case}', DFS(row, col))