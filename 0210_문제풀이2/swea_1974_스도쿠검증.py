def check_sudoku(arr):
    for i in range(9):  # 행열 검증
        if len(set([arr[i][j] for j in range(9)])) != 9:
            return 0
        elif len(set([arr[j][i] for j in range(9)])) != 9:
            return 0

    for i in [0, 3, 6]:  # 3x3 검증
        for j in [0, 3, 6]:
            if len(set([arr[i + k][j + l] for k in range(3) for l in range(3)])) != 9:
                return 0
    return 1

for test_case in range(1,int(input())+1):
    arr = [input().split() for _ in range(9)]
    print(f'#{test_case}', check_sudoku(arr))