import sys;sys.stdin=open('input.txt', 'r')

def move_ladder(r, c, move_dir):
    # 좌, 우, 하
    dr = [0, 0, 1]
    dc = [-1, 1, 0]

    for i in range(3):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < 100 and 0 <= nc < 100 and dc[i] != move_dir:
            if M[nr][nc] == 1:                              # 인점한 경로에 1이 있는 경우
                move_dir = dc[i] * (-1) if i < 2 else 10
                return move_ladder(nr, nc, move_dir) + 1    # 재귀함수 호출하고 + 1 -> 호출된 횟수만큼 +1 될것
    else:
        return 0                                            # 인접한 경로에 1이 없는 경우 리턴

for _ in range(10):
    test_case = input()

    M = [list(map(int, input().split())) for _ in range(100)]

    min_val, c_idx = 999999, 0
    for col in range(100):
        if M[0][col] == 1:
            val = move_ladder(0, col, 10)
            if min_val >= val:
                min_val, c_idx = val, col

    print(f'#{test_case}', c_idx)