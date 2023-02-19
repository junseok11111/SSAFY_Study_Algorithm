# import sys;sys.stdin=open('input.txt', 'r')

for test_case in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))

    total = 0
    for idx in range(2, N-2):

        high_b = 0
        for n in [-2, -1, 1, 2]:    # 양 옆 2칸 빌딩 높이 중 최대값 찾기
            if high_b < lst[idx+n]:
                high_b = lst[idx+n]

        result = lst[idx]-high_b    # 현재 빌딩과 양옆 빌딩 중 최대 높이를 가진 빌딩 간 높이 차이

        if result > 0:              # 높이 차이가 양수인 경우 (현재 빌딩의 높이가 더 높은 겨우)
            total += result

    print(f'#{test_case} {total}')