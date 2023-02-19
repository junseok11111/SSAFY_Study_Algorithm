import sys;sys.stdin=open('input.txt', 'r')

def mv_dal(r, c):
    # 우,하,좌,상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    s, f, dir = 0, N, 0         # dir: 닯팽이가 움직여야 하는 방향 설정하는 변수
    for num in range(1, N*N + 1):
        nr = r + dr[dir%4]      # 4로 나눈 나머지로 해야, 반복적으로 0, 1, 2, 3을 얻을 수 있음
        nc = c + dc[dir%4]

        if s <= nr < f and s <= nc < f and matrix[nr][nc] == 0: # 범위조건 만족하고 가는 방향에 0이 있으면
            matrix[r][c] = num
            r, c = nr, nc
        else:
            matrix[r][c] = num
            dir += 1            # 방향 전환
            r = r + dr[dir%4]
            c = c + dc[dir%4]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    matrix = [[0] * N for _ in range(N)]
    mv_dal(0, 0)

    print(f'#{test_case}')
    for lst in matrix:
        print(*lst)
