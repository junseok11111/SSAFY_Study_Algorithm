import sys;sys.stdin=open('input.txt', 'r')

# 카운팅 정렬
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))
    b = [0]*N

    k = 0
    for num in a:
        if k < num:
            k = num

    cnt = [0]*(k + 1)

    # 자료의 빈도수를 계산
    for val in a:
        cnt[val] += 1

    # 누적합 계산
    for i in range(1, k + 1):
        cnt[i] = cnt[i - 1] + cnt[i]

    # 누적합을 활용하여 새로운 배열에 숫자 정렬
    for val in a:
        cnt[val] -= 1
        b[cnt[val]] = val

    print(f'#{test_case}', *b)

