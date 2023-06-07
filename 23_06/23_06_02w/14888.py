# 연산자 끼워넣기 ( 정답 )
# 알고리즘 : 완전탐색(풀이), 백트래킹

from itertools import permutations

n = int(input())
a = list(map(int, input().split()))
# + - * //
cals = list(map(int, input().split()))

cal_list = []
for i in range(4):
    for j in range(cals[i]):
        cal_list.append(i)

com = permutations(cal_list, n-1)

answer = []
for cal in com:
    temp = a[0]
    for i in range(n-1):

        if cal[i] == 0:
            temp = temp + a[i+1]
        elif cal[i] == 1:
            temp = temp - a[i+1]
        elif cal[i] == 2:
            temp = temp * a[i+1]
        else:
            if temp < 0:
                temp = -((-temp) // a[i+1])
            else:
                temp = temp // a[i+1]
    answer.append(temp)

print(max(answer))
print(min(answer))
