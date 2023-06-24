# 탑 ( 정답, 알고리즘 확인 )
# 알고리즘 : 스택
# 뒤에서부터 높이와 위치를 함께 저장
# 스택에 현재 빌딩 높이보다 낮은 건물이 있으면 위치 저장 뒤 pop

from collections import deque

n = int(input())
buildings = list(map(int, input().split()))
answers = [0 for _ in range(n+1)]

dq = deque()
dq.append((buildings[-1], n))
for i in range(n-2, -1, -1):
    while True:
        if len(dq) == 0:
            break
        elif dq[-1][0] < buildings[i]:
            answers[dq[-1][1]] = i+1
            dq.pop()
        else:
            break
    dq.append((buildings[i], i+1))


print(*answers[1:])
