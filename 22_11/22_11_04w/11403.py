# 경로 찾기 ( 오답 )


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answerArr = [[0 for _ in range(n)] for _ in range(n)]


def dfs(x):
    global temp
    for i in range(n):
        if arr[x][i] == 1 and not visited[i]:
            visited[i] = True
            answerArr[x][i] = 1
            temp.append(i)
            dfs(i)


for i in range(n):
    visited = [False for _ in range(n)]
    temp = []
    temp.append(i)
    dfs(i)
    for i in range(len(temp)):
        for j in range(i+1, len(temp)):
            answerArr[temp[i]][temp[j]] = 1

for i in answerArr:
    for j in i:
        print(j, end=" ")
    print()
