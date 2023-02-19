# 중위표기법 -> 후위표기법 변환시 필요한 것
#   - 연산자 우선순위 (스택 안, 스택 밖)
#   - 후위표기법 저장할 곳
#   - 빈 스택

# 우선 순위
isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 0}       # in-stack priority    : 스택 안 연산자의 우선순위
icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3, ')': 0}       # in-coming priority   : 들어오는 토큰의 우선순위

for test_case in range(1, 11):
    N = int(input())    # 문장의 길이
    infix = input()     # 중위표기법 문장
    postfix = ''        # 후위표기법 저장할 곳
    S = []              # 빈 스택

    # 중위표기법 -> 후위표기법 변환 방법
    for token in infix:
        if token in '+-*/()':                                   # token이 연산자인 경우 '+-*/()'

            if token == ')':                                    # token이 닫는 괄호, ')'일 때
                while S[-1] != '(':                             # 스택에 여는괄호 '('가 나올때까지
                    postfix += S.pop()                          # 스택에 pop()하여 반환된 값을 postfix에 추가
                S.pop()                                         # 반복문이 끝나면, pop()을 하여 스택에 여는괄호 제거

            else:                                               # token이 '+-*/(' 인 경우
                if S:                                           # 스택이 비어있지 않으면 (우선순위 비교)
                    if icp[token] <= isp[S[-1]]:                # 스택 안의 연산자의 우선순위가 토큰의 우선순위보다 높은 경우
                        while S and icp[token] <= isp[S[-1]]:   # 스택이 비거나,토큰의 우선순위가 스택 안의 연산자의 우선순위보다 높을 경우 반복문 빠져나감.
                            postfix += S.pop()                  # 그렇지 않으면 계속 스택에 pop()하여 반환된 값을 postfix에 추가
                S.append(token)                                 # 이후 스택에 token 추가 (스택이 비어있는 경우에는 무조건 스택에 token 추가)

        else:                                                   # token이 피연산자(숫자)인 경우
            postfix += token                                    # postfix에 token 추가

    while S:                                                    # 스택이 비어있을 때까지
        postfix += S.pop()                                      # 스택 안의 연산자를 pop하여 postfix에 추가

    # 후위표기법 계산
    for token in postfix:
        if token in '+-*/':                         # TOKEN이 연산자인 경우
            b = int(S.pop())                        # 스택안의 숫자를 꺼냄
            a = int(S.pop())                        # 이때 꺼내는 순서를 고려해야 함.
            if token == '+': S.append(a + b)        # 나중에 꺼낸는 숫자를 연산자의 왼쪽에 오게해줌
            elif token == '-': S.append(a - b)      # 고려 안하면 , 빼기, 나누기에서 문제 발생
            elif token == '*': S.append(a * b)
            else: S.append(a // b)                  # 나누기의 경우, 모든 경우에서 나누어 떨어진다는 조건하에 이렇게 쓸 수 있음

        else:                                       # 피연산자(숫자)의 경우
            S.append(token)                         # 무조건 스택에 추가

    print(f'#{test_case}', S[0])                    # 최종적으로 스택에 남은 값이 계산값에 해당