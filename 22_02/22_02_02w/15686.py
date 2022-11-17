# 치킨배달 ( 정답 )
# 치킨집 m 개 선택하는 경우의수 모두 치킨거리 구해서 최솟값 찾기


import sys
from itertools import combinations

# N,M 입력
n,m = map(int,sys.stdin.readline().split())

# 배열 입력
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if arr[i][j]==0:
            continue
        # 집
        elif arr[i][j]==1:
            house.append([i,j])
        # 치킨집
        else:
            chicken.append([i,j])

# print(house)
# print(chicken)


# 입력상태 치킨거리 구하는 코드
#chickenlen=[[0 for _ in range(len(chicken))] for _ in range(len(house))]
# for i in range(len(house)):
#     for j in range(len(chicken)):
#         chickenlen[i][j] = abs(house[i][0]-chicken[j][0]) + abs(house[i][1]-chicken[j][1])

# for i in range(len(house)):
#     for j in range(len(chicken)):
#         print(chickenlen[i][j], end=" ")
#     print()




# m 개 치킨집 배열 넣어주면 치킨거리 계산
def countmin(array):
    minval=0
    minarr=[[0 for _ in range(len(array))] for _ in range(len(house))]
    for i in range(len(house)):
        for j in range(len(array)):
            minarr[i][j] = abs(house[i][0]-array[j][0]) + abs(house[i][1]-array[j][1])
    for i in range(len(house)):
        minval+=min(minarr[i])
        # print(min(minarr[i]))
    return minval
    

# countmin(chicken)


# m개 치킨집 배열만 만들면 됨

# 실패해서 combinations 사용

# 가능한 조합 저장
comb = list(combinations(chicken,m))

# 각 조합의 치킨거리 저장
temp=[]

for i in range(len(comb)):
    temp.append(countmin(comb[i]))
print(min(temp))
