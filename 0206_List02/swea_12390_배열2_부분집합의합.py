import sys;sys.stdin=open('input.txt', 'r')

# A : 1 ~ 12
T = int(input())
for test_case in range(1, T+1):
    A = list(range(1, 13))
    N, K = map(int, input().split())

    total = 0
    for i in range(1<<12):
        set_sum = 0
        cnt = 0

        # 비트연산자를 활용한 부분집합 생성
        for j in range(12):
            if i&(1<<j):
                set_sum += A[j]
                cnt += 1

            if cnt > N: # 부분집합의 갯수가 N보다 크면 break
                break
        else:
            if cnt == N and set_sum == K:
                total += 1
    print(f'#{test_case}', total)