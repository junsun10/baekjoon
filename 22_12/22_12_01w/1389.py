# 케빈 베이컨의 6단계 법칙 ( 정답 )
# 알고리즘 : BFS
# 각 친구까지의 거리를 BFS로 탐색

from collections import deque

n, m = map(int, input().split())
arr = [[0 for _ in range(n+1)] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1


def bfs(end):
    dq = deque()
    visited = [False for _ in range(n+1)]
    dq.append([start])
    visited[start] = True
    tempAnswer = []
    while dq:
        arrNow = dq.popleft()
        x = arrNow[-1]
        for i in range(1, n+1):
            if i == end and arr[x][i] == 1:
                temp = arrNow[:]
                temp.append(i)
                visited[i] = True
                tempAnswer.append(temp)
            elif i != x and arr[x][i] == 1 and not visited[i]:
                temp = arrNow[:]
                temp.append(i)
                visited[i] = True
                dq.append(temp)
    return tempAnswer


answer = []
for start in range(1, n+1):
    count = 0
    for end in range(1, n+1):
        if start != end:
            bridge = bfs(end)
            getMin = []
            minLen = n
            for i in bridge:
                if len(i) < minLen:
                    getMin = i[:]
                    minLen = len(i)
            count += minLen-1
    answer.append(count)
temp = n*n
minIndex = 0
for i in range(n):
    if answer[i] < temp:
        temp = answer[i]
        minIndex = i
print(minIndex+1)
