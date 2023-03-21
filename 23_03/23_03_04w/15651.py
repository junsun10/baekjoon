# N과 M (3) ( 정답 )
# 알고리즘 : 백트래킹

n, m = map(int, input().split())

answer = []
depth = 0


def dfs():
    global depth

    if depth == m:
        print(*answer)
        return

    for i in range(1, n+1):
        answer.append(i)
        depth += 1
        dfs()
        answer.pop()
        depth -= 1


dfs()
