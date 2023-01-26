# 최소비용 구하기 ( 정답 )
# 알고리즘 : 다익스트라
# deque로 구현했을 때 시간초과 -> heapq 사용

import heapq

n = int(input())
m = int(input())
info = [[] for _ in range(n+1)]
for _ in range(m):
    f, t, c = map(int, input().split())
    info[f].append([t, c])
start, end = map(int, input().split())

visited = [False for _ in range(n+1)]
min_cost = [100000*100001 for _ in range(n+1)]
queue = []
heapq.heappush(queue, (start, 0))
visited[start] = True
min_cost[start] = 0

while queue:
    now, cost = heapq.heappop(queue)
    if cost > min_cost[end]:
        continue
    for t, c in info[now]:
        if t != end and cost + c > min_cost[end]:
            continue
        elif t == end:
            min_cost[end] = min(min_cost[end], cost+c)
        elif not visited[t]:
            heapq.heappush(queue, (t, cost+c))
            visited[t] = True
            min_cost[t] = cost+c
        else:
            if cost+c < min_cost[t]:
                heapq.heappush(queue, (t, cost+c))
                min_cost[t] = cost+c

print(min_cost[end])
