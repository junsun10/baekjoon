# 쿼드트리

import sys
input = sys.stdin.readline
limit_number = 10000
sys.setrecursionlimit(limit_number)

n = int(input())
in_arr = [list(map(int,input().strip())) for _ in range(n)]
answer = []
print(in_arr)

def re(x,y,l):
    global answer

    temp = []
    count0 = 0
    count1 = 0
    for i in range(x,x+l,1):
        for j in range(y,y+l,1):
            temp.append(in_arr[i][j])
            if in_arr[i][j] == 0:
                count0 += 1
            else:
                count1 += 1
    print()
    print(temp)
    print(x,y,l)
    print(count0, count1)
    if count0 == l*l:
        answer.append([0,l])
    elif count1 == l*l:
        answer.append([1,l])
    else:
        if l//2 >= 2 and x+l//2<=n and y+l//2<=n:
            print("call 4")
            re(x,y,l//2)
            re(x,y+l//2,l//2)
            re(x+l//2,y,l//2)
            re(x+l//2,y+l//2,l//2)
        else:
            print("append temp")
            temp.append(l)
            answer.append(temp)

        


re(0,0,n)

print(answer)

new_answer = []

temp = answer[0][-1]
temp_answer = [answer[0][:-1]]
count = 1

for i in range(1,len(answer),1):
    if len(temp_answer) == 4:
        new_answer.append(temp_answer)
        temp_answer = [answer[i][:-1]]
        temp = answer[i][-1]
        count = 0

    elif answer[i][-1] == temp:
        count += 1
        temp_answer.append(answer[i][:-1])
    else:
        new_answer.append(temp_answer)
        temp_answer = [answer[i][:-1]]
        temp = answer[i][-1]
        count = 0

    print(temp, temp_answer)
        
new_answer.append(temp_answer)
print(new_answer)

# for i in range(len(new_answer)):
#     for j in range(new_answer[i]):