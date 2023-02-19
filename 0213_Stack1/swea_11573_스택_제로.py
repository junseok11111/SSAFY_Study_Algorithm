def push(n):
    global top
    top += 1
    S[top] = n

def pop():
    global top
    top = top - 1 if top >= 0 else -1

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    S = [0] * 30
    top = -1

    for idx in range(N):
        if lst[idx] != 0:   # 0 이 아닌 숫자가 오는 경우
            push(lst[idx])  # push
        else:               # 0 이 오면
            pop()           # pop
    print(f'#{test_case}', sum(S[:top+1]))