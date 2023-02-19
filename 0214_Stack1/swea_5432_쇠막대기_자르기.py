# import sys;sys.stdin=open('input.txt', 'r')
T = int(input())
for test_case in range(1, T+1):
    string = input()
    cnt = total = 0
    for idx in range(len(string)):
        if string[idx] == '(':      # ( 가 오는 경우 cnt +1
            cnt += 1
        elif string[idx] == ')':    # ) 가 오는 경우, 레이저인지 쇠막대기 끝인지 구분 필요
            cnt -= 1                # 레이저든 쇠막대기 끝이든 우선 cnt - 1
            total = total + cnt if string[idx-1] == '(' else total + 1  # 레이저로 자른 막대기 갯수를 total에 더해줌
    print(f'#{test_case}', total)