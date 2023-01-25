# 조합 ( 정답 )
# 알고리즘 : 수학

n, m = map(int, input().split())
answer = 1
for i in range(m):
    answer *= n-i
for i in range(m):
    answer = answer // (m-i)
print(answer)
