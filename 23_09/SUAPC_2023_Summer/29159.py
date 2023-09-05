# 케이크 두 개 ( 정답 )
# 알고리즘: 수학
# 두 직사각형의 무게중심을 지나는 직선 구하기

from math import gcd
from fractions import Fraction

temp = []
for _ in range(4):
    temp.append(list(map(int, input().split())))

temp.sort()


cake1_x = Fraction((temp[3][0] + temp[0][0]), 2)
cake1_y = Fraction((temp[3][1] + temp[0][1]), 2)

temp = []
for _ in range(4):
    temp.append(list(map(int, input().split())))

temp.sort()


cake2_x = Fraction((temp[3][0] + temp[0][0]), 2)
cake2_y = Fraction((temp[3][1] + temp[0][1]), 2)

p = Fraction((cake2_y - cake1_y), (cake2_x - cake1_x))
print(p, end=" ")
q = cake1_y - (p*cake1_x)
print(q)
