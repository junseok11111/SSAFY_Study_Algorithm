import sys;sys.stdin=open('input.txt', 'r')


def find_min(*n):   # 최소값 찾는 함수
    minVal = n[0]
    for v in n:
        if minVal > v: minVal = v
    return minVal


for test_case in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))
    K = 100
    C = [0] * (K + 1)

    for val in arr:     # 빈도수 계산
        C[val] += 1

    s, l = 0, K
    while C[s] == 0: s += 1     # 배열 C의 0이 아닌 숫자가 맨 처음 나오는 index -> 가장 낮은 box 높이
    while C[l] == 0: l -= 1     # 배열 C의 0이 아닌 숫자가 맨 마지막에 나오는 index -> 가장 높은 box 높이

    while dump != 0 and l - s > 1:               # dump가 0인 경우 또는 l - s가 1 이하인 경우 둘중 하나라도 false면 반복문 멈춤
        min_val = find_min(dump, C[s], C[l])    # 두 숫자 C[s]. C[l] 와 dump 수 비교 -> 가장 작은 값 찾기
        # 가장 작은 값 기준으로 해서 C[s], C[l]은 해당 값만큼 빼주고, C[s+1], C[l-1]은 해당 값만큼 더해줌
        dump -= min_val
        C[s], C[s+1] = C[s] - min_val, C[s+1] + min_val
        C[l], C[l-1] = C[l] - min_val, C[l-1] + min_val
        if not C[s]: s += 1
        if not C[l]: l -= 1
    print(f'#{test_case}', l-s)

"""
# 교수님ver. 1

def min_max(arr):
    min_idx = max_idx = 0
    for i in range(len(arr)):
        if arr[min_idx] > arr[i]:
            min_idx = i
        if arr[max_idx] < arr[i]:
            max_idx = i
    return min_idx, max_idx

for test_case in range(1, int(input())):

    dump = map(int, input().split())
    arr = list(map(int, input().split()))

    # dump 횟수만큼 반복
    for i in range(dump)

        # arr 에서 최대/최소값의 인덱스 찾아서
        min_idx, max_idx = min_max(arr)
        arr[max_idx] -= 1
        arr[min_idx] += 1

    min_dix, max_idx = min_max(arr)
    print(f'#{test_case}', arr[max_idx]) - arr[min_idx])

"""