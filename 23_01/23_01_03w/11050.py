# 이항 계수 1 ( 알고리즘 검색 )
# 알고리즘 : 수학
# n!/(k!(n-k)!)

n, k = map(int, input().split())
a = 1
b = 1
for i in range(n, k, -1):
    a *= i
for i in range(1, n-k+1):
    b *= i
print(a//b)
