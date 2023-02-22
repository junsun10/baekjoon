# 개수 세기 ( 정답 )
# 알고리즘 : 구현

n = int(input())
arr = list(map(int, input().split()))
v = int(input())
answer = 0

for i in arr:
    if i == v:
        answer += 1
print(answer)
