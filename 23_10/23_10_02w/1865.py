# 웜홀 ( 정답, 알고리즘 검색, 반례 검색 )
# 알고리즘: 플로이드 워셜, 벨만 포드
# 음의 가중치가 존재하므로 다익스트라 사용 불가능

for _ in range(int(input())):

    n, m, w = map(int, input().split())
    path = [[[] for _ in range(n+1)] for _ in range(n+1)]

    for _ in range(m):
        s, e, t = map(int, input().split())
        path[s][e].append(t)
        path[e][s].append(t)

    for _ in range(w):
        s, e, t = map(int, input().split())
        path[s][e].append(-t)

    dist = [[int(1e9) for _ in range(n+1)] for _ in range(n+1)]

    # dist 초기화
    for i in range(1, n+1):
        for j in range(1, n+1):
            # 웜홀이 자기 자신으로 가는 경우도 고려해야 함
            # if i == j:
            #     dist[i][j] = 0
            if len(path[i][j]) > 0:
                dist[i][j] = min(path[i][j])
            else:
                continue

    available = False

    # 플로이드 워셜
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
                # 시간초과 해결위해 음수 사이클 존재하면 탈출
                if dist[i][i] < 0:
                    available = True
                    break
            if available:
                break
        if available:
            break

    if available:
        print("YES")
    else:
        print("NO")
