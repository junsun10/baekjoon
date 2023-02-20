# N 과 M (2) ( 정답 )
# 알고리즘 : 백트래킹

n, m = map(int, input().split())
answer = []


def dfs(x):
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return

    for i in range(x+1, n+1):
        answer.append(i)
        dfs(i)
        answer.pop()


dfs(0)
