def find_winner(s, e):
    if s == e:
        return arr[s], s
    mid = (s+e)//2
    a = find_winner(s, mid)
    b = find_winner(mid+1, e)
    if a[0] - b[0] in [1, 1, -2]: return a
    elif a[0] == b[0]: return a
    else: return b

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{test_case}', find_winner(0, N-1)[1]+1)