# LCS 2 ( 메모리초과 )
# 최장 공통 부분 수열
# 각각 부분수열 구해서 긴것부터 있는지 비교

import sys
from itertools import combinations


s1 = list(sys.stdin.readline().strip())
s2 = list(sys.stdin.readline().strip())

# print(s1)
# print(s2)

find = False
answer = ""
for i in range(len(s1),-1,-1):
    # print()
    sub1 = list(combinations(s1,i))
    sub2 = list(combinations(s2,i))
    # print(sub1)
    # print(sub2)
    for j in sub1:
        if j in sub2:
            # print(j)
            answer = j
            find = True
            break
    if find:
        break

# print(j,type(j))
# print(len(j))
# print(j[0])
answer_string = ""

for i in answer:
    answer_string += i

print(len(answer_string))
print(answer_string)