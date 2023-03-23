# 차이를 최대로 ( 정답 )
# 알고리즘 : 백트래킹

n = int(input())
arr = list(map(int, input().split()))

answer_l = []
answer = 0
visited = [False for _ in range(n)]
depth = 0


def f():
    temp = 0
    for i in range(len(answer_l)-1):
        temp += abs(answer_l[i]-answer_l[i+1])
    return temp


def dfs():
    global depth, answer
    if depth == n:
        answer = max(answer, f())
        return

    for i in range(n):
        if not visited[i]:
            answer_l.append(arr[i])
            visited[i] = True
            depth += 1
            dfs()
            answer_l.pop()
            visited[i] = False
            depth -= 1


dfs()
print(answer)
