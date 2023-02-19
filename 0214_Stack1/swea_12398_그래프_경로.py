def DFS(v, g):
    if v == g: return 1     # 목표에 도착한 경우, 리턴 1
    visited[v] = 1

    for w in G[v]:
        if not visited[w]:  # 아직 방문하지 않은 경우
            if DFS(w, g):   # 재귀호출, 만일 리턴값 1이면
                return 1    # 리턴 1
    return 0


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)               # 유향 그래프이기에 한 방향의 값만 저장

    s, g = map(int, input().split())
    visited = [0] * (V + 1)          # 방문 기록, 방문했으면 1 아니면 0
    print(f'#{test_case}', DFS(s, g))