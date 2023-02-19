import sys;sys.stdin=open('input.txt', 'r')
# 같은 색의 box는 겹치지 않고 다른색의 box만 겹칠 수 있기에
# 이차원의 빈 배열에 대해서
# 각 box에 해당하는 좌표에 +1을 해주면
# 색이 겹치는 부분은 2의 값을 가질 것

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    matrix = [[0 for _ in range(10)] for _ in range(10)]

    total = 0
    for _ in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split()))
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                matrix[i][j] += 1
                if matrix[i][j] == 2:   # 겹치는 부분 확인하는 조건
                    total += 1          # 맞으면 count

    print(f'#{test_case}', total)