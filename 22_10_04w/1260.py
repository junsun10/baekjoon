# DFS와 BFS
# 알고리즘 : DFS, BFS
# DFS, BFS 구현


from collections import deque

n, m, v = map(int, input().split())

arr = []
for i in range(m):
    x, y = map(int, input().split())
    arr.append([x, y])
    arr.append([y, x])
arr.sort()


def dfs():
    now = dq.popleft()

    for x, y in arr:
        if now == x and not visited[y]:
            visited[y] = True
            dq.append(y)
            answer.append(y)
            dfs()
        elif now == y and not visited[x]:
            visited[x] = True
            dq.append(x)
            answer.append(x)
            dfs()


def bfs():

    while (dq):
        now = dq.popleft()

        for x, y in arr:
            if now == x and not visited[y]:
                visited[y] = True
                dq.append(y)
                answer.append(y)
            elif now == y and not visited[x]:
                visited[x] = True
                dq.append(x)
                answer.append(x)


visited = [False for _ in range(n+1)]
dq = deque()
dq.append(v)
visited[v] = True
answer = []
answer.append(v)
dfs()
for i in answer:
    print(i, end=" ")
print()

visited = [False for _ in range(n+1)]
dq = deque()
dq.append(v)
visited[v] = True
answer = []
answer.append(v)
bfs()
for i in answer:
    print(i, end=" ")
print()
