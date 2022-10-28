# LCS 2 

# 

import sys



s1 = list(sys.stdin.readline().strip())
s2 = list(sys.stdin.readline().strip())

# s1 = sys.stdin.readline().strip()
# s2 = sys.stdin.readline().strip()

answer = []
for k in range(len(s1)):
    temp = [(-1,-1)]
    for i in range(k,len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j] and temp[-1][-1]<j:
                temp.append((s2[j],j))
                break
    temp = temp[1:]
    if temp in answer:
        continue
    else:
        answer.append(temp)

# print(answer)
answer_string = ""

for i in answer[0]:
    answer_string += i[0]

print(len(answer_string))
if len(answer_string)!=0:
    print(answer_string)




