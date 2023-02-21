import sys;sys.stdin = open('input.txt')
from collections import deque
for _ in range(10):
    test_case = input()
    N = 16
    arr = [input() for _ in range(N)]

    for row in range(N):
        if '2' in arr[row]:
            s_coord = (row, arr[row].index('2'))
            break

    visited = [[0]*N for _ in range(N)]
    Q = deque()

    visited[s_coord[0]][s_coord[1]] = 1
    Q.append(s_coord)

    ans = 0
    while Q:
        r, c = Q.popleft()
        if arr[r][c] == '3':
            ans = 1
            break

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != '1':

                if not visited[nr][nc]:
                    visited[nr][nc] = 1
                    Q.append((nr, nc))
    print(f'#{test_case}', ans)
