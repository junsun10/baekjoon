# 숨바꼭질 ( 정답 검색 )
# 알고리즘 : BFS
# 세가지 경우를 BFS

from collections import deque

n, k = map(int, input().split())
visited = [False for _ in range(100001)]

dq = deque()
if k == n:
    print(0)
elif k < n:
    print(n-k)
else:
    dq.append((n, 0))

    while True:
        index, time = dq.popleft()
        if index == k:
            print(time)
            break
        else:
            if index*2 <= 100000 and not visited[index*2]:
                dq.append((index*2, time+1))
                visited[index*2] = True
            if index-1 >= 0 and not visited[index-1]:
                dq.append((index-1, time+1))
                visited[index-1] = True
            if index+1 <= 100000 and not visited[index+1]:
                dq.append((index+1, time+1))
                visited[index+1] = True
