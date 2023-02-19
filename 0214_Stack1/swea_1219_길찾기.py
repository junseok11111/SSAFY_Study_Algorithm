# import sys;sys.stdin=open('input.txt', 'r')
for _ in range(10):
    test_case, N = map(int, input().split())
    arr = list(map(int, input().split()))
    # 간선에 대한 정보를 토대로 인접리스트를 만듬 (유향)
    G = [[arr[j + 1] for j in range(0, 2*N, 2) if i == arr[j]] for i in range(N)]
    visited = [0] * 100     # 방문 기록
    S, v = [0], 0           # 스택, 출발값

    while S:
        visited[v] = 1
        if v == 99: break           # 도착한 경우, break
        for w in G[v]:
            if not visited[w]:      # 방문 기록이 없으면
                S.append(v)         # v를 스택에 추가
                v = w               # v에 w를 할당
                break
        else:
            v = S.pop()             # for문이 break 없이 끝난 경우, pop

    print(f'#{test_case}', visited[99])