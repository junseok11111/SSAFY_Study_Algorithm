import sys;sys.stdin=open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    M, N = len(str1), len(str2)

    ans = 0
    for i in range(N-M+1):
        if str1[0] == str2[i]:      # str2의 i번째 알파벳이 str1의 첫번째 알파벳과 일치하는 경우
            p_str2 = ''             
            for j in range(M):      # str2의 i번째 부터, str1의 단어 길이만큼 해당 구간의 알파벳을 따로 저장
                p_str2 += str2[i+j]
            if str1 == p_str2:      # 비교하여 str1과 일치할 경우, 1
                ans = 1
                break
    print(f'#{test_case}', ans)