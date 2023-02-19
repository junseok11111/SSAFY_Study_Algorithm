import sys;sys.stdin=open('input.txt', 'r')
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    for i in range(N-1):    # 선택정렬
        if i % 2:           # 홀수는 오름차순으로 정렬
            minIdx = i
            for j in range(i+1, N):
                if lst[minIdx] > lst[j]:
                    minIdx = j
            lst[i], lst[minIdx] = lst[minIdx], lst[i]
        else:               # 짝수는 내림차순으로 정렬
            maxIdx = i
            for j in range(i+1, N):
                if lst[maxIdx] < lst[j]:
                    maxIdx = j
            lst[i], lst[maxIdx] = lst[maxIdx], lst[i]
    print(f'#{test_case}', *lst[:10])

