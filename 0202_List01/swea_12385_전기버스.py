# import sys;sys.stdin=open('input.txt', 'r')
for test_case in range(1, int(input())+1):
    K, N, M = map(int, input().split())
    A = list(map(int, input().split()))

    C = [0] * (N + 1 + K)
    for val in A:           # 노선의 정류장 위치 인덱스 표시
        C[val] += 1

    bus, charge = 0, 0  # bus의 초기 위치, 충전 횟수
    while bus + K < N:                              # 만약 버스의 최대 이동 범위가 종점보다 큰 경우 반복문 종료
        for c_station in range(bus+K, bus, -1):     # 버스의 이동 범위, 최대 이동범위에서 역순으로
            if C[c_station]:            # 만약 충전소가 있는 경우 (C[c_station] == 1)
                bus = c_station         # bus의 위치를 충전소 위치로 재설정
                charge += 1             # 충전 횟수 추가
                break                   # for 문 빠져나오기

        else:           # for 문이 온전히 끝난경우,(충전소가 없는 경우)
            charge = 0  # 충전횟수 초기화
            break       # while 반복문 종료

    print(f'#{test_case} {charge}')


"""
# 전기버스 다른 방법 (아마도 교수님 풀이)
for test_case in range(1, int(input())+1):
    K, N, M = map(int, input().split())
    # [1, 3, 5, 7, 9]
    # [0] + [1, 3, 5, 7, 9] + [N] 출발점, 종점 고려
    arr = [0] + list(map(int, input().split())) + [N]
    # 1. 안되는 경우 인접한 두 충전소의 거리가 K보다 크면 절대 못감

    cur = ans = 0
    for i in range(1, M + 2):
        if arr[i-1] + K < arr[i]:
            ans = 0
            break

        if cur + K < arr[i]:
            cur = arr[i - 1]
            ans += 1

    print(f'#{test_case}', ans)
"""