# 소수의 연속합 ( 알고리즘 확인 )
# 알고리즘: 에라토스테네스의 체
# 에라토스테네스의 체를 사용해 n까지의 소수를 모두 구한 뒤
# 연속합 경우의 수 탐색
# 에라토스테네스의 체를 사용하지 않으면 시간초과

from math import sqrt


n = int(input())

answer = 0
num = [True for _ in range(n+1)]
num[0] = False
num[1] = False

# 에라토스테네스의 체
arr = []
for i in range(1, int(sqrt(n))+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1

    if count == 2:
        arr.append(i)

for i in arr:
    temp = i

    while temp <= n:
        num[temp] = False
        temp += i

# 걸러지고 남은 소수 추가
for index, value in enumerate(num):
    if value:
        arr.append(index)

# 연속합 가능한 경우의 수 탐색
for i in range(len(arr)):
    temp = 0
    for j in range(i, len(arr)):
        if temp + arr[j] == n:
            answer += 1
            break
        elif temp + arr[j] < n:
            temp += arr[j]
        else:
            break

print(answer)
