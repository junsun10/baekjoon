# N과 M (1)

n, m = map(int, input().split())
visited = [False for _ in range(n+1)]
answer = []


def dfs():
    if len(answer) == m:
        print(*answer)
        return

    for i in range(1, n+1):
        if not visited[i]:
            answer.append(i)
            visited[i] = True
            dfs()
            answer.pop()
            visited[i] = False


dfs()
