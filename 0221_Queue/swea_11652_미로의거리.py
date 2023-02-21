import sys;sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    visited = [[0]*N for _ in range(N)]     # 방문 기록

    s_coord = ()                            # 출발 좌표 구하기
    for row in range(N):
        for col in range(N):
            if arr[row][col] == '2':
                s_coord = (row, col)
                break
        if s_coord:
            break

    Q = deque()
    Q.append(s_coord)                       # 출발 좌표를 Q에 추가
    visited[s_coord[0]][s_coord[1]] = 1     # visited 의 출발좌표에 1

    ans = 0
    while Q:                                # Q가 비어있으면 반복문 종료
        r, c = Q.popleft()
        if arr[r][c] == '3':                # 도착지에 도착한 경우
            ans = visited[r][c] - 2         # 출발지점에서 포함한 1과 도착지점의 1을 빼줘야 하기에
            break

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 상하좌우
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != '1':  # 범위 벗어나거나 배열 값이 1인 경우는 포함하지 않음
                if not visited[nr][nc]:
                    Q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1 # 이동거리 + 1

    print(f'#{test_case}', ans)



