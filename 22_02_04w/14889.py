# 스타트와 링크 ( 정답 )
# 팀이 이루어지는 조합을 구함
# 팀에서 두명씩 짝을 짓는 조합을 구함
# 구한 조합으로 점수 계산

import sys
from itertools import combinations

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split(" "))))

# 두명 조합에 대한 딕셔너리
dic = {}
for x in range(n-1):
    for y in range(x+1,n):
        dic[(x,y)] = arr[x][y] + arr[y][x]
# print(dic)

person_list = []
for i in range(n):
    person_list.append(i)

# 팁 경우의 수      ex) [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
comb_team = list(combinations(person_list,n//2))
# print(comb_team)

# 팀 조합       ex) [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
match_team = []
for i in range(len(comb_team)//2):
    match_team.append((comb_team[i],comb_team[-i-1]))
# print(match_team)

score = []
for i in range(len(match_team)):
    score1 = 0
    score2 = 0
    # 한팀에 3명 이상이면 둘씩 짝지어줘야함
    comb1 = list(combinations(match_team[i][0],2))
    comb2 = list(combinations(match_team[i][1],2))
    for j in comb1:
        score1 += dic[j]
    for j in comb2:
        score2 += dic[j]
    # print(score1, score2)
    score.append(abs(score1-score2))

print(min(score))

