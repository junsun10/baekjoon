# 이항 계수 2 ( 정답 )
# 알고리즘 : 수학
# 파스칼의 삼각형을 사용해 dp로도 구현 가능

n, k = map(int, input().split())
answer = 1
for i in range(n-k+1, n+1):
    answer = answer * i
for i in range(1, k+1):
    answer = answer // i
print(answer % 10007)
