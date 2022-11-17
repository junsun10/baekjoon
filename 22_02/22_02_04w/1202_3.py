# 보석 도둑 ( 정답 )

import sys
import heapq

# n: 보석개수 k: 가방개수
n,k = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
arr.sort()

b = [int(sys.stdin.readline()) for _ in range(k)]
b.sort()

answer = 0
temp = []
for i in range(k):

    # 배낭무게보다 작은 보석들 모두 temp에 저장
    # 배낭 무게가 오름차순이므로 한번 들어간 보석은
    # 그 뒤 모든 배낭무게보다 작음
    while arr and b[i] >= arr[0][0]:
        heapq.heappush(temp,-arr[0][1])
        heapq.heappop(arr)
    
    # 저장된 보석 중 가장 비싼 것 pop
    if temp:
        answer += heapq.heappop(temp)
    elif not arr:
        break

print(-answer)