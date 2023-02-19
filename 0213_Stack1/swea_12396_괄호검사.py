T = int(input())
for test_case in range(1, T+1):
    string = input()
    group1 = [ch for ch in string if ch in '(){}']
    top = -1
    S = [0] * len(group1)

    ans = 1
    for j in group1:
        if j in '({':                                   # ({ 의 경우 push
            top += 1
            S[top] = j

        else:                                           # ({ 가 아닌 경우
            if top >= 0:                                # 스택이 차있는 경우
                if j == ')' and S[top] == '(': top -= 1
                elif j == '}' and S[top] == '{': top -= 1
                else: ans = 0; break
            else: ans = 0; break                        # 스택이 비어있는 경우

    if top != -1: ans = 0                               # 스택이 비어있지 않은 경우, 0
    if group1 == []: ans = 0                              # string에 괄호가 없는 경우
    print(f'#{test_case}', ans)