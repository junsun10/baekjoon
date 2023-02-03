# N과 M (8) ( 정답 )
# 알고리즘 : 백트래킹

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = []


def dfs():
    if answer[0] == m:
        for i in range(1, m+1):
            print(answer[i][0], end=" ")
        print()
        return

    for i in range(answer[-1][1], n):
        answer.append([arr[i], i])
        answer[0] += 1
        dfs()
        answer.pop()
        answer[0] -= 1


for i in range(n):
    answer = [1, [arr[i], i]]
dfs()
