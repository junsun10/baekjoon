# ATM
# 알고리즘 : 정렬, 그리디
# 시간 적은 순서로 정렬 후 누적 시간 계산

n = int(input())

people = list(map(int, input().split()))

people.sort()

answer = 0
temp = 0

for i in people:
    temp += i
    answer += temp

print(answer)
