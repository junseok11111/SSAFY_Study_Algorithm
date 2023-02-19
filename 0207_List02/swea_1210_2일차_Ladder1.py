import sys;sys.stdin=open('input.txt', 'r')

def move_ladder(r, c, m_dir):
    # 좌, 우, 상 -> 좌우다 확인하고 그 다음 위를 확인해야 함
    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    for i in range(3):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < 100 and 0 <= nc < 100 and dc[i] != m_dir:  # m_dir은 왔던 길 방향에 대한 정보를 담은 변수
            if M[nr][nc] == 1:
                m_dir = dc[i] * (-1) if i < 2 else 10
                result = move_ladder(nr, nc, m_dir)             # 아직 1만 나오는 경우 재귀호출
                return result
    else:
        return c                                                # 좌, 우, 상에 1이 없는 경우, 해당 좌표를 리턴

for _ in range(10):
    test_case = input()

    M = [list(map(int, input().split())) for _ in range(100)]

    for col in range(100):
        if M[99][col] == 2:                                     # 목표 지점부터 위로 사다리타고 올라감
            val = move_ladder(99, col, 10)
            print(f'#{test_case}', val)
            break