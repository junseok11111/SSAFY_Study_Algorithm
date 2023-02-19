def push(n):
    global top
    top += 1
    S[top] = n


def pop():
    global top
    top -= 1


for test_case in range(1, 11):
    N, string = input().split()
    S = [0] * int(N)
    top = -1

    for i in range(int(N)):
        if top == -1:
            push(string[i])

        else:
            if S[top] != string[i]: # 스택 안의 값과 들어오는 문자가 같지 않은 경우
                push(string[i])     # push
            else:                   # 그렇지 않으면
                pop()               # pop

    print(f'#{test_case}', ''.join(S[:top+1]))