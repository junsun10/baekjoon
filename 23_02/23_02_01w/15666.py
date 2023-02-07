# N과 M (12) ( 정답 )
# 알고리즘 : 백트래킹

n, m = map(int, input().split())
arr = list(map(int, input().split()))
# 중복된 수 제거
new_set = set(arr)
arr = list(new_set)
arr.sort()
answer = []


def dfs(x):
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return

    # 중복으로 뽑을 수 있으므로 x부터 시작
    for i in range(x, len(arr)):
        answer.append(arr[i])
        dfs(i)
        answer.pop()


dfs(0)
