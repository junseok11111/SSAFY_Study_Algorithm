# N : 0 ~ 9 가 적혀있는 카드
# 가장 많은 카드에 적힌 숫자, 카드는 몇장?
# 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력

import sys;sys.stdin=open('input.txt', 'r')
T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    A = input()
    K = 9
    C = [0] * (K + 1)

    # 갯수 세기
    for val in A:
        C[int(val)] += 1

    max_val, card_num = 0, 0 # max_val : 갯수, card_num : 숫자
    for idx in range(K + 1):    # idx = card_num
        if max_val <= C[idx]:   # 같다는 조건 있어야 카드 장수가 같을 때 적힌 숫자가 큰 쪽을 출력
            max_val = C[idx]
            card_num = idx

    print(f'#{test_case} {card_num} {max_val}')
