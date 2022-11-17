# 숨바꼭질 ( 정답1 )
# 거꾸로

import sys
from collections import deque

# N,K 입력
n,k = map(int,sys.stdin.readline().split())

visited = []
queue = deque()
# 큐에 (값,초) 저장
queue.append((k,0))

if n==k:
    print(0)
else:
    while queue:
        # 값, 초
        popvalue, second = queue.popleft()

        # 짝수일때
        if popvalue%2==0:
            # 세가지 경우에 n이 있으면 break
            if popvalue+1 == n or popvalue-1 == n or popvalue//2 == n:
                print(second + 1)
                break
            else:
                # 방문 안했을 경우만 ( 해당값, 초+1 ) 추가
                if popvalue+1 not in visited:
                    visited.append(popvalue+1)
                    queue.append((popvalue+1,second+1))
                if popvalue-1 not in visited and popvalue-1 >= n:
                    visited.append(popvalue-1)
                    queue.append((popvalue-1,second+1))
                if popvalue//2 not in visited:
                    visited.append(popvalue//2)
                    queue.append((popvalue//2,second+1))
        
        # 홀수일때 (2로 나누는 경우 제외)
        else :
            # 두가지 경우에 n이 있으면 break
            if popvalue+1 == n or popvalue-1 == n:
                print(second + 1)
                break
            else:
                # 방문 안했을 경우만 ( 해당값, 초+1 ) 추가
                if popvalue+1 not in visited:
                    visited.append(popvalue+1)
                    queue.append((popvalue+1,second+1))
                if popvalue-1 not in visited and popvalue-1 >= n:
                    visited.append(popvalue-1)
                    queue.append((popvalue-1,second+1))

            # print(queue)
        