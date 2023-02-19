import sys;sys.stdin=open('input.txt', 'r')

def find_num(Px):   # Px 값을 찾아야
    cnt = 0         # 탐색한 횟수
    l, r = 1, P
    while l <= r:
        c = int((l + r) / 2)
        if c == Px:
            cnt += 1
            return cnt  # 찾으면 return
        elif c < Px:    # 찾는 값이 더 큰 경우
            l = c       # 시작점을 이동
            cnt += 1
        else:           # 찾는 값이 작은 겨우
            r = c       # 끝 지점을 이동
            cnt += 1
    return 100

T = int(input())
for test_case in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    Pa_cnt = find_num(Pa)
    Pb_cnt = find_num(Pb)

    if Pa_cnt < Pb_cnt:
        print(f'#{test_case} A')
    elif Pa_cnt > Pb_cnt:
        print(f'#{test_case} B')
    else:
        print(f'#{test_case} 0')