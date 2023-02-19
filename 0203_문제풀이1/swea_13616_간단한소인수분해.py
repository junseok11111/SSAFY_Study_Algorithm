import sys;sys.stdin=open('input.txt', 'r')
T = int(input())
divs = [2, 3, 5, 7, 11]
# 변하지 않는 값은 반복문 안에 넣을 필요 X

for test_case in range(1, T + 1):
    N = int(input())
    cnts = [0]*len(divs)

    for i in range(len(divs)):
        while N%divs[i] == 0:
            cnts[i] += 1
            N = N//divs[i]

    print(f'#{test_case}', *cnts)