# 숨바꼭질 ( 정답2 )
# 방문안한값만 큐에 더함


import sys
from collections import deque

# N,K 입력
n,k = map(int,sys.stdin.readline().split())

visited = [False for _ in range (100001)]
queue = deque()
# 큐에 (값,초) 저장
queue.append((n,0))

if n==k:
    print(0)
else:
    while queue:
        # 값, 초
        popvalue, second = queue.popleft()

        # 세가지 경우에 k가 있으면 break
        if popvalue+1 == k or popvalue-1 == k or popvalue*2 == k:
            print(second + 1)
            break

        else:
            # 방문 안했을 경우만 ( 해당값, 초+1 ) 추가
            if 0 <= popvalue+1 <= 100000:
                if visited[popvalue+1] == False:
                    visited[popvalue+1] = True
                    queue.append((popvalue+1,second+1))
            if 0 <= popvalue-1 <= 100000:
                if visited[popvalue-1] == False:
                    visited[popvalue-1] = True
                    queue.append((popvalue-1,second+1))
            if 0 <= popvalue*2 <= 100000:      # 이 조건이 가능한 이유를 모르겠음
                if visited[popvalue*2] == False:
                    visited[popvalue*2] = True
                    queue.append((popvalue*2,second+1))

            # print(queue)
        
