# 경로 찾기 ( 정답 )
# 알고리즘 : DFS
# 큐에 지금까지 지나온 경로 저장해 aswerArr 갱신

from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answerArr = [[0 for _ in range(n)] for _ in range(n)]


def dfs(t):
    global dq
    while (dq):
        x, li = dq.popleft()

        for i in range(n):
            if arr[x][i] == 1 and not visited[i]:
                visited[i] = True
                temp = li[:]
                temp.append(i)
                for j in li:
                    answerArr[j][i] = 1
                if i != li[0]:
                    dq.append((i, temp))


for i in range(n):
    visited = [False for _ in range(n)]
    dq = deque()
    dq.append((i, [i]))
    dfs(i)

for i in answerArr:
    for j in i:
        print(j, end=" ")
    print()
