# N과 M (5) ( 정답, 알고리즘 검색 )
# 알고리즘 : 백트래킹

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = []
visited = [False for _ in range(n)]


def dfs():
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr.append(nums[i])
            dfs()
            visited[i] = False
            arr.pop()


dfs()
