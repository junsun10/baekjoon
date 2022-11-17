# 예산 ( 정답 )
# 1) 요청예산 합이 예산보다 낮으면 최댓값 출력
# 2) 각 지방의 요청예산을 정렬
# 3) 한개 씩 빼면서 남은 금액으로 상한액 계산
# 4) 상한액이 다음 값보다 작을때까지 진행

import sys
from collections import deque

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())

arr.sort()
queue = deque()
for i in arr:
    queue.append(i)

# 요청예산 합
sum_money = sum(arr)

# 요청대로 배정 가능
if sum_money <= m:
    print(max(arr))

# 최솟값을 상한액으로 해도 불가능한 경우
elif queue[0]*n > m:
    print(m//n)

else:
    for i in range(n-1):
        temp = queue.popleft()
        # 상한액이 다음 값보다 작을때까지 진행
        # (m-temp)//(n-(i+1)) : 상한액
        if (m-temp)//(n-(i+1)) >= queue[0]:
            m -= temp
            continue
        else:
            print((m-temp)//(n-(i+1)))
            break