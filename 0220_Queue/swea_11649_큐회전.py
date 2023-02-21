import sys;sys.stdin=open('input.txt', 'r')

#선형 Queue
"""
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
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    Q = [0] * (N + M)
    front = rear = -1

    for num in arr:
        enQueue(num)

    for _ in range(M):
        enQueue(deQueue())

    print(f'#{test_case}', Q[front+1])
"""

# 원형 Queue
"""
def enQueue(item):
    global rear, N
    rear = (rear + 1) % N
    Q[rear] = item


def deQueue():
    global front
    front = (front + 1) % N
    return Q[front]


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))
    front = -1
    rear = N - 1

    for _ in range(M):
        enQueue(deQueue())

    print(f'#{test_case}', Q[(front+1) % N])
"""


# deque
from collections import deque

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int,input().split()))
    Q = deque()

    for num in arr:
        Q.append(num)

    for _ in range(M):
        Q.append(Q.popleft())

    print(f'#{test_case}', Q[0])


