import sys;sys.stdin=open('input.txt', 'r')

# delta 활용
def adj_sum(i, j):
    #하,상,우,좌
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    total = 0
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N: # 인덱스 범위 조건
            total += lst[ni][nj]        # 이웃원소 합 계산
    return total

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    max_val, max_xy = 0,()

    for i in range(N):
        for j in range(N):      # 이차원 배열의 모든 값에 대해 탐색
            val = adj_sum(i, j)
            if max_val < val:   # 최대값 비교
                max_val = val
                max_xy = (i, j) # 최대값을 갖는 좌표 저장
    print(f'#{test_case}', max_xy[0], max_xy[1], max_val)

