# 최대공약수와 최소공배수 ( 정답 )
# 알고리즘 : 수학

a, b = map(int, input().split())
gcd = 0
lcm = 0
if a > b:
    a, b = b, a

for i in range(1, a+1):
    if a % i == 0 and b % i == 0:
        gcd = i

lcm = gcd * (a//gcd) * (b//gcd)
print(gcd)
print(lcm)
