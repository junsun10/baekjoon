# 부등호 ( 정답 )
# 알고리즘 : 완전 탐색, 백트래킹
# 숫자의 배열 가능한 경우의 수 모두 탐색
# 각 경우의 수에서 부등호 조건에 맞는 경우만 정답에 저장

from itertools import permutations

k = int(input())
arr = list(map(str, input().split()))

list = permutations([i for i in range(10)], k+1)
answers = []

for i in list:
    temp = i[:]
    check = True
    for j in range(1, len(temp)):
        if arr[j-1] == "<":
            if temp[j-1] < temp[j]:
                continue
            else:
                check = False
                break
        else:
            if temp[j-1] > temp[j]:
                continue
            else:
                check = False
                break

    if check:
        temp = ""
        for j in i:
            temp += str(j)
        answers.append(int(temp))

max_val = max(answers)
min_val = min(answers)

if len(str(max_val)) == k:
    print("0"+str(max_val))
else:
    print(max_val)

if len(str(min_val)) == k:
    print("0"+str(min_val))
else:
    print(min_val)
