import sys;sys.stdin=open('input.txt', 'r')


def enQueue(item):
    global rear
    rear = (rear + 1) % 8
    Q[rear] = item


def deQueue():
    global front
    front = (front + 1) % 8
    return Q[front]


for _ in range(10):
    test_case = input()
    rear, front = 7, -1
    Q = list(map(int, input().split()))

    num = 0
    while Q[rear] != 0:
        val = deQueue() - (num%5 + 1)
        num += 1
        if val <= 0: enQueue(0)
        else: enQueue(val)
    print(f'#{test_case}', *Q[front+1:], *Q[:rear+1])