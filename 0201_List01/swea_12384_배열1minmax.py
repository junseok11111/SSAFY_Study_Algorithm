T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    max_val, min_val = lst[0], lst[0]

    for value in lst:
        if max_val < value: # 최대값과 비교
            max_val = value

        if min_val > value: # 최소값과 비교
            min_val = value

    print(f'#{test_case} {max_val - min_val}')