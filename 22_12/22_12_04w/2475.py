# 검증수 ( 정답 )
# 알고리즘 : 구현

nums = list(map(int, input().split()))
answer = 0
for num in nums:
    answer += num**2
print(answer % 10)
