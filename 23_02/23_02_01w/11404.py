# 플로이드 ( 정답 )
# 알고리즘 : 플로이드 워셜
# 문제 의도는 플로이드 워셜이었으나 다익스트라 반복해 구현

import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])

distances = [[100000*(n+1) for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    queue = []
    heapq.heappush(queue, [0, i])
    distances[i][i] = 0

    while queue:
        distance, now = heapq.heappop(queue)

        if distances[i][now] < distance:
            continue

        for d, to in graph[now]:
            if distances[i][to] > distance + d:
                distances[i][to] = distance + d
                heapq.heappush(queue, [distance + d, to])

for i in range(n+1):
    for j in range(n+1):
        if distances[i][j] == 100000*(n+1):
            distances[i][j] = 0

for i in range(1, n+1):
    print(" ".join(map(str, distances[i][1:])))
