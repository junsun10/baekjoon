# 치긴 배달 ( 정답 )
# 알고리즘 : 구현, 완전탐색
# 치킨집 별 거리 계산한 뒤
# m개 선택 모든 조합 계산

from collections import deque
from itertools import combinations

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append([i, j])
        elif arr[i][j] == 2:
            chicken.append([i, j, len(chicken)])

# 치킨집 별 거리 계산
chicken_length = []
for i in range(len(chicken)):
    temp = []
    x, y, z = chicken[i]
    for j in range(len(house)):
        hx, hy = house[j]
        temp.append(abs(x-hx)+abs(y-hy))
    chicken_length.append(temp)

# m개 선택후 최솟값 계산
answer = []
list = combinations(chicken, m)
for i in list:
    temp = [n*n for _ in range(len(house))]
    for l in range(len(house)):
        for j in i:
            z = j[2]
            temp[l] = min(temp[l], chicken_length[z][l])
    answer.append(sum(temp))
print(min(answer))
