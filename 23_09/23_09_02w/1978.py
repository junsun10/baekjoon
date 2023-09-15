# 소수 찾기 ( 정답 )
# 알고리즘: 수학

from math import sqrt

n = int(input())
arr = list(map(int, input().split()))
answer = 0

for x in arr:
    count = 0
    for i in range(1, int(sqrt(x))+1):
        if x % i == 0:
            count += 1
    if count == 1 and x != 1:
        answer += 1
print(answer)
