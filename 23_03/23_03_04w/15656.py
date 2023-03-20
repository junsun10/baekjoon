# N과 M (7) ( 정답 )
# 알고리즘 : 백트래킹

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

depth = 0
answer = []


def dfs():
    global depth

    if depth == m:
        for i in answer:
            print(i, end=" ")
        print()
        return

    for i in range(len(arr)):
        answer.append(arr[i])
        depth += 1
        dfs()
        answer.pop()
        depth -= 1


dfs()
