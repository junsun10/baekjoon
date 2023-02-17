# 최단경로 ( 정답 )
# 알고리즘 : 다익스트라
# 힙을 사용해 다익스트라 구현

import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])
distance = [3000001 for _ in range(V+1)]

queue = []
heapq.heappush(queue, (0, K))
distance[K] = 0

while queue:
    val, now = heapq.heappop(queue)

    for v, w in graph[now]:
        if distance[v] > val + w:
            distance[v] = val + w
            heapq.heappush(queue, (val+w, v))

for i in range(1, V+1):
    if distance[i] == 3000001:
        print("INF")
    else:
        print(distance[i])
