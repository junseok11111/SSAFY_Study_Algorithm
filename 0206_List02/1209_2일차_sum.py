for _ in range(1, 11):
    test_case = input()

    lst = [list(map(int, input().split())) for _ in range(100)]

    max_val = 0
    # 가로행에 대한 합
    for i in range(100):
        total = 0
        for j in range(100):
            total += lst[i][j]

        if max_val < total:
            max_val = total
    
    # 세로열에 대한 합
    for i in range(100):
        total = 0
        for j in range(100):
            total += lst[j][i]

        if max_val < total:
            max_val = total

    total1, total2 = 0, 0
    # 두 대각선의 합
    for i in range(100):
        total1 += lst[i][i]
        total2 += lst[99-i][i]

    if max_val < total1:
        max_val = total1

    if max_val < total2:
        max_val = total2

    print(f'#{test_case}', max_val)