import sys;sys.stdin=open('input.txt', 'r')

def spin(matrix):   # 90도 회전
    return [[matrix[r][c] for r in range(N-1, -1, -1)] for c in range(N)]

def join_lst(lst):
    result = ''
    for i in lst:result += i
    return result

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [input().split() for _ in range(N)]

    spin_90 = spin(matrix)
    spin_180 = spin(spin_90)
    spin_270 = spin(spin_180)

    print(f'#{test_case}')
    for i in range(N):
        print(join_lst(spin_90[i]), join_lst(spin_180[i]), join_lst(spin_270[i]))