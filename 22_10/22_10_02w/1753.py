# 최단경로 ( 메모리 초과 )
#
#
from collections import deque
V, E = map(int, input().split())
K = int(input())
arr = [list(map(int, input().split())) for _ in range(E)]
# 간선 배열
arrE = [[-1 for _ in range(V+1)] for _ in range(V+1)]
for u, v, w in arr:
    if arrE[u][v] != -1:
        if arrE[u][v] > w:
            arrE[u][v] = w
    elif arrE[u][v] == -1:
        arrE[u][v] = w
for i in range(1, V+1):
    arrE[i][i] = 0


def bfs(end):
    if K == end:
        return 0
    answerList = []
    visited = [False for _ in range(V+1)]
    visited[K] = True
    endInK = False
    dq = deque()
    dq.append((K, 0))
    while dq:
        u, w = dq.popleft()
        for i in range(1, V+1):
            if arrE[u][i] != -1 and not visited[i]:
                if i == end:
                    answerList.append(w+arrE[u][i])
                    endInK = True
                dq.append((i, w+arrE[u][i]))
                visited[i] = True
    if endInK:
        return min(answerList)
    else:
        return "INF"


for i in range(1, V+1):
    answer = bfs(i)
    print(answer)
