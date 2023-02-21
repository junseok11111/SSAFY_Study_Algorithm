import sys;sys.stdin=open('input.txt', 'r')
# 화덕에 가장 마지막까지 남아있는 피자 번호

def enQueue(item):
    global rear
    rear += 1
    Q[rear] = item


def deQueue():
    global front
    front += 1
    return Q[front]


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())                # N: 화덕의 크기, M: 피자의 개수
    Ci = list(enumerate(map(int, input().split()))) # M개의 피자에 뿌려진 치즈의 양
    Q = [0] * 500
    rear = front = -1
    for i in range(N):
        enQueue(Ci[i])

    while rear - front != 1:
        Ci_amount = deQueue()
        if Ci_amount[1]//2:
            enQueue((Ci_amount[0], Ci_amount[1]//2))
        else:
            if N < M:
                enQueue(Ci[N]); N += 1
    print(f'#{test_case}', Q[rear][0]+1)
