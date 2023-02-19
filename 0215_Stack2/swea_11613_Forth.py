dic = {'+': 1, '-': 2, '*': 3, '/': 4}

T = int(input())
for test_case in range(1, T+1):
    arr = input().split()

    S = []
    ans = 'error'
    for token in arr:
        if token in dic:
            if len(S) > 1:
                b = S.pop()
                a = S.pop()
                if a not in dic and b not in dic:
                    if dic[token] == 1:S.append(int(a) + int(b))
                    elif dic[token] == 2:S.append(int(a) - int(b))
                    elif dic[token] == 3:S.append(int(a) * int(b))
                    else:S.append(int(int(a) / int(b)))
                else:break
            else:break

        elif token == '.' and len(S) == 1:
            ans = S[0]
        else:
            S.append(token)
    print(f'#{test_case}', ans)