# 모든 순열 ( 정답 )
# 알고리즘 : 백트래킹

n = int(input())

answer = []
visited = [False for _ in range(n+1)]
depth = 0


def dfs():
    global depth
    if depth == n:
        print(*answer)
        return

    for i in range(1, n+1):
        if not visited[i]:
            answer.append(i)
            visited[i] = True
            depth += 1
            dfs()
            answer.pop()
            visited[i] = False
            depth -= 1


dfs()
