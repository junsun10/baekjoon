# 나의 FIFA 팀 가치는? ( 정답 )
# 알고리즘: 힙
# 선발을 뽑고 가치를 계산하는 과정을
# 최대힙을 사용해 해결

import heapq

n, k = map(int, input().split())
arr = [[] for _ in range(12)]
for i in range(n):
    p, w = map(int, input().split())
    heapq.heappush(arr[p], -w)

for _ in range(k):

    for i in range(1, 12):
        if len(arr[i]) > 0:
            temp = heapq.heappop(arr[i]) * -1
            if temp > 0:
                heapq.heappush(arr[i], -(temp-1))

answer = 0
for i in range(1, 12):
    if len(arr[i]) > 0:
        answer += heapq.heappop(arr[i]) * -1
print(answer)
