def push(n):
    global top
    top += 1
    S[top] = n


def pop():
    global top
    top -= 1


T = int(input())
for test_case in range(1, T+1):
    string = input()
    S = [0] * len(string)
    top = -1

    for ch in string:
        if top == -1:
            push(ch)
        else:
            if S[top] != ch:    # 들어오는 문자와 스택의 top번째 있는 문자와 다른 경우
                push(ch)        # 문자를 스택에 푸쉬
            else:               # 같으면
                pop()           # pop으로 제거

    print(f'#{test_case}', top+1)