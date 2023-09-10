# 개똥벌레 ( 정답 )
# 알고리즘: 누적합
# 석순과 종유석을 나눠서 계산
# 누적합 사용해 높이에 따른 장애물 개수 파악

n, h = map(int, input().split())

b = [0 for _ in range(h)]
t = [0 for _ in range(h)]

for i in range(n):
    val = int(input())
    if i % 2 == 0:
        b[val-1] += 1
    else:
        t[-val] += 1

for i in range(h-2, -1, -1):
    b[i] += b[i+1]

for i in range(1, h):
    t[i] += t[i-1]

arr = [0 for _ in range(h)]
for i in range(h):
    arr[i] = b[i] + t[i]

min_val = min(arr)
answer = 0
for i in arr:
    if i == min_val:
        answer += 1

print(min_val, answer)
