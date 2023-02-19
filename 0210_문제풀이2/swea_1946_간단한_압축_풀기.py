T = int(input())
for test_case in range(1, T+1):
    string = ''
    for i in range(int(input())):
        word, num = input().split()
        string += word * int(num)

    N = len(string)//10 if not len(string)%10 else len(string)//10 + 1
    print(f'#{test_case}')
    for num in range(0, N):
        print(string[10*num:10+10*num])