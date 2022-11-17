# 최단경로 ( 시간 초과 )
#
#
from collections import deque
V, E = map(int, input().split())
K = int(input())
answerList = [200000 for _ in range(V+1)]
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

# for i in range(V):
#     print(arrE[i])


def bfs():
    # visited = [False for _ in range(V+1)]
    # visited[K] = True
    dq = deque()
    dq.append((K, 0))
    while dq:
        # print(dq)
        u, w = dq.popleft()
        for nU, nW in arrE[u]:
            # if not visited[nU]:
            #     dq.append((nU, w+nW))
            #     visited[nU] = True
            #     if answerList[nU] > w+nW:
            #         answerList[nU] = w+nW

            if answerList[nU] > w+nW:
                dq.append((nU, w+nW))
                answerList[nU] = w+nW
        # print(answerList)


bfs()
answerList[K] = 0

for i in range(1, V+1):
    if answerList[i] != 200000:
        print(answerList[i])
    else:
        print("INF")
