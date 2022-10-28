# 동전 0
# 알고리즘 : 그리디
# 큰 값의 동전부터 빼기


n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

answer = 0

for i in range(n-1, -1, -1):
    while (k >= 0):
        if k >= coin[i]:
            k -= coin[i]
            answer += 1
        else:
            break
    if k == 0:
        break

print(answer)
