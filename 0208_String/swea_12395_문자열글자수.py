import sys;sys.stdin=open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    str1 = list(set(input()))   # 똑같은 알파벳 탐색하는 것 방지
    str2 = input()
    N = len(str1)

    max_cnt = 0
    for i in range(N):
        cnt = 0
        for j in str2:
            if str1[i] == j:
                cnt += 1        # 동일한 알파벳인 경우 count

        if max_cnt < cnt:
            max_cnt = cnt

    print(f'#{test_case}', max_cnt)


