import sys;sys.stdin=open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    
    for i in range(N-1):                # 선택정렬 (오름차순)
        minIdx = i                      # 최소값을 갖는 인덱스 설정 (i)
        for j in range(i+1, N):         # 인덱스 i 이후의 값과 값 비교
            if lst[minIdx] > lst[j]:    # 가장 작은 값을 갖는 값의 인덱스 저장
                minIdx = j
        lst[i], lst[minIdx] = lst[minIdx], lst[i]   # 가장 작은 값을 갖는 인덱스와 i번째 인덱스의 값을 교환
    print(f'#{test_case}', *lst)