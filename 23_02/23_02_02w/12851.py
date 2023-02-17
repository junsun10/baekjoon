# 숨바꼭질 2 ( 정답 )
# 알고리즘 : bfs
# 이동한 위치가 이전보다 빨리 도착하면 갱신
# bfs과정에서 도착하는 최소 시간이 동일해도 추가해야
# 정답 경우의 수 계산 가능

from collections import deque

n, k = map(int, input().split())

if n > k:
    print(n-k)
    print(1)
elif n == k:
    print(0)
    print(1)
else:
    queue = deque()
    queue.append((n, 0))
    dp = [100001 for _ in range(100001)]
    dp[n] = 0
    answers = []

    while queue:
        now, time = queue.popleft()

        if now == k:
            answers.append(time)

        if now*2 <= 100000 and now*2 < k*2 and dp[now*2] >= time + 1:
            queue.append((now*2, time+1))
            dp[now*2] = time+1
        if now+1 <= 100000 and now+1 <= k and dp[now+1] >= time + 1:
            queue.append((now+1, time+1))
            dp[now+1] = time+1
        if now-1 >= 0 and dp[now-1] >= time + 1:
            queue.append((now-1, time+1))
            dp[now-1] = time+1

    print(answers[0])
    print(len(answers))
