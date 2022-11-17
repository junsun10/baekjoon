# 최단경로 ( 알고리즘 검색 )
# 알고리즘: 다익스트라
# 우선순위 큐를 사용한 다익스트라 알고리즘으로 시작지점에서 각 노드별 최단거리 갱신

import heapq
from collections import deque
V, E = map(int, input().split())
K = int(input())
# 간선 배열
arrE = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    find = False
    for i, t in enumerate(arrE[u]):
        tV, tW = t[0], t[1]
        if tV == v:
            if tW <= w:
                find = True
                break
            else:
                arrE[u][i][1] = w
                break
    if not find:
        arrE[u].append([v, w])


def dijkstra(graph, start):
    # 최단거리 배열 초기화
    distances = [float('inf') for _ in range(V+1)]
    distances[start] = 0
    # 우선순위 큐
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        # print(distances)
        # print(queue)
        current_distance, current_destination = heapq.heappop(queue)
        # 기존 거리보다 길다면 통과
        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination]:
            # 새 경로의 길이
            distance = current_distance + new_distance
            # 새 경로가 현재보다 짧다면 갱신
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances


answer = dijkstra(arrE, K)
for i in range(1, V+1):
    if answer[i] == float('inf'):
        print("INF")
    else:
        print(answer[i])
