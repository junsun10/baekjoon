# LCS 2 ( 메모리 초과 )

# 안겹치는 알파벳 빼고 짧은길이만큼 조합해서 비교

import sys
from itertools import combinations
from collections import deque



s1 = list(sys.stdin.readline().strip())
s2 = list(sys.stdin.readline().strip())

# s1 = sys.stdin.readline().strip()
# s2 = sys.stdin.readline().strip()


if len(s1)>len(s2):
    temp = s1
    s1=s2
    s2=temp

# print(s1)
# print(s2)

new_s2 = []
for i in s2:
    new_s2.append(i)
len_s2 = len(s2)
for i in range(len_s2):
    if s2[i] not in s1:
        new_s2.remove(s2[i])
        print(s2[i],new_s2)



# print(s1)
# print(new_s2)


temp = 0
if len(s1)>len(new_s2):
    temp = len(new_s2)
else:
    temp = len(s1)

answer = 0

for i in range(temp,0,-1):
    sub1 = list(combinations(s1,i))
    sub2 = list(combinations(new_s2,i))
    # print(sub1)
    # print(sub2)


    find = False

    for j in sub1:
        if j in sub2:
            answer = j
            find = True
            break
    if find:
        break

answer_string = ""

for i in answer:
    answer_string += i

print(len(answer_string))
print(answer_string)