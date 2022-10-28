# 최단경로 ( 메모리 초과 )
#
#
from collections import deque
V, E = map(int, input().split())
K = int(input())
arr = [list(map(int, input().split())) for _ in range(E)]
# 간선 배열
arrE = [[] for _ in range(V+1)]
for u, v, w in arr:
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


def bfs(end):
    if K == end:
        return 0
    answer = 200000
    visited = [False for _ in range(V+1)]
    visited[K] = True
    endInK = False
    dq = deque()
    dq.append((K, 0))
    minW = 0
    while dq:
        u, w = dq.popleft()
        for nU, nW in arrE[u]:
            if nU == end:
                answer = min(answer, w+nW)
                endInK = True
            else:
                dq.append((nU, w+nW))
                visited[nU] = True
    if endInK:
        return answer
    else:
        return "INF"


for i in range(1, V+1):
    answer = bfs(i)
    print(answer)
