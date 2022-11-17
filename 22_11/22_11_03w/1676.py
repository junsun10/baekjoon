# 팩토리얼 0의 개수 ( 정답 )
# 알고리즘 : 구현
# 간단한 구현

n = int(input())
factorial = 1

for i in range(1, n+1):
    factorial *= i

answer = 0
while (True):
    if factorial % 10 == 0:
        answer += 1
        factorial = factorial // 10
    else:
        break
print(answer)
