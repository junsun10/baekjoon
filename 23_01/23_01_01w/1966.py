# 프린터 큐 ( 정답 )
# 알고리즘 : 큐, 구현
# 우선순위 개수를 저장해 자신보다 우선순위 높은 케이스가 있는지 확인

from collections import deque

for _ in range(int(input())):
    count = 0
    n, m = map(int, input().split())
    priority_count = [0 for _ in range(10)]
    queue = deque()
    arr = list(map(int, input().split()))
    for i in range(n):
        queue.append([i, arr[i]])
        priority_count[arr[i]] += 1

    while True:
        pop_val, priority = queue.popleft()
        if priority == 9:
            priority_count[priority] -= 1
            count += 1
            if pop_val == m:
                print(count)
                break
        else:
            temp = sum(priority_count[priority+1:])
            if temp == 0:
                priority_count[priority] -= 1
                count += 1
                if pop_val == m:
                    print(count)
                    break
            else:
                queue.append([pop_val, priority])
