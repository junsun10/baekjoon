# 최소비용 구하기 ( 정답 )
# 알고리즘 : 다익스트라
# 다익스트라 검색해서 구현

import heapq

n = int(input())
m = int(input())
info = [[] for _ in range(n+1)]
for _ in range(m):
    f, t, c = map(int, input().split())
    info[f].append([t, c])
start, end = map(int, input().split())

min_cost = [100000*100001 for _ in range(n+1)]
min_cost[start] = 0
queue = []
heapq.heappush(queue, [start, 0])

while queue:
    print(queue)
    now, cost = heapq.heappop(queue)

    if cost > min_cost[end]:
        continue

    for t, c in info[now]:
        if cost + c < min_cost[t]:
            min_cost[t] = cost + c
            heapq.heappush(queue, [t, cost + c])

print(min_cost[end])
