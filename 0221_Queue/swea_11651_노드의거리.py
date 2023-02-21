import sys;sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())    # 노드 개수, 간선 개수

    G = [[] for _ in range(V+1)]        # 인접리스트
    for _ in range(E):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    s, g = map(int, input().split())
    visited = [0] * (V + 1)     # 방문 정보 (최단 이동 거리)
    Q = deque()                 # 빈 Q
    visited[s] = 1              # 우선 시작 지점 방문 기록 작성
    Q.append(s)                 # Q에 시작 지점 추가

    ans = 0
    while Q:                                    # Q가 비는 경우 멈춤
        v = Q.popleft()                         # Q의 가장 첫번째의 요소를 꺼내 v에 할당

        if v == g:                              # v가 목표 노드인 경우
            ans = visited[g] - 1                # ans에 최단 이동 거리 할당
            break                               # 반복문 빠져나옴

        for w in G[v]:                          # v에 연결된 노드 확인
            if not visited[w]:                  # w의 방문기록이 없다면
                visited[w] = visited[v] + 1     # 이동 거리
                Q.append(w)                     # 해당 노드를 Q에 추가
    print(f'#{test_case}', ans)

# 교수님 코드
"""
for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)] # 정점번호 1 ~ V
 
    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)  # 주의: 무향 그래프
        G[v].append(u)
    s, g = map(int, input().split())
 
    visited = [0] * (V+1)
    D = [0] * (V+1)  # 출발점에서 각정점까지 최단거리
 
    Q = []
    # 시작점을 방문하고 큐에 삽입
    Q.append(s)
    visited[s] = 1
 
    while Q:        #빈큐가 아닐동안
        v = Q.pop(0)
        # v의 방문하지 않은 인접정점들을 모두 찾아서
        for w in G[v]:
            if not visited[w]:
                Q.append(w)   # w를 큐에 삽입, 방문표시
                # visited[w] = 1
                # # v ---> w
                D[w] = D[v] + 1
                visited[w] = visited[v] + 1
 
    if visited[g]:
        visited[g] -= 1
    print(f'#{tc} {visited[g]}')
"""