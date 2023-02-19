T = int(input())
for test_case in range(1, T+1):
    lst = list(input())
    N = len(lst)
    for i in range(N//2):           # 해당 단어의 절반을 기준으로
        if lst[i] != lst[N-1-i]:    # 대칭되는 지점을 비교
            print(f'#{test_case}', 0)
            break
    else:
        print(f'#{test_case}', 1)

# 플래그 변수 활용
# T = int(input())
# for test_case in range(1, T+1):
#     lst = list(input())
#     N = len(lst)
#
#     ans = 1 # 플래그 변수
#     for i in range(N//2):
#         if lst[i] != lst[N-1-i]:
#             ans = 0
#             break
#     print(f'#{test_case}', ans)