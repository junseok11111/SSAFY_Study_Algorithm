import sys;sys.stdin=open('sample_input.txt', 'r')

for test_case in range(1, int(input())+1):
    t, p = input().split()
    N, M = len(t), len(p)
    i = j = cnt = 0
    while i < N:
        if t[i] != p[j]:    # t의 i번째 문자와, p의 j번째 문자가 일치하지 않는 경우
            i = i - j + 1
            j = 0
        else:               # t의 i번째 문자와, p의 j번째 문자가 일치하는 경우
            i += 1          # 그 다음 문자도 확인
            j += 1
        if j == M:          # 만일 j가 M이라면, p의 단어가 일치함을 확인한 것이기에
            cnt += 1        # 카운팅
            j = 0           # j는 초기화
    print(f'#{test_case}', N - (M * cnt) + cnt)

