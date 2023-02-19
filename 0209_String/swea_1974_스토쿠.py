def check(m)->list:
    # 가로, 세로 체크
    for i in range(9):
        r_lst = [m[i][j] for j in range(9)]
        c_lst = [m[j][i] for j in range(9)]
        if len(set(r_lst)) != 9 or len(set(c_lst)) != 9:    # 가로 또는 세로열에 대하여 중복된 숫자가 있다면
            return 1                                        # 1을 리턴
    
    # 3x3 체크
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            b_lst = [m[i+k][j+l] for k in range(3) for l in range(3)]
            if len(set(b_lst)) != 9:return 1    # 3x3에 중복된 숫자가 있는 경우, 1을 리턴
 
for test_case in range(1,int(input())+1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
     
    ans = 0 if check(matrix) else 1
    print(f'#{test_case}', ans)