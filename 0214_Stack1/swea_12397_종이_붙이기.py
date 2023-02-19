def func(N):
    if N in dic:
        return dic[N]
    dic[N] = (func(N-2) * 2) + func(N-1)    # 점화식
    return dic[N]

dic = {0:0, 1:1, 2:3}                       # 메모이제이션
for test_case in range(1, int(input())+1):
    N = int(input())//10
    print(f'#{test_case}', func(N))