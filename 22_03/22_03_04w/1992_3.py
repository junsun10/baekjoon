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

    if l > 2 and x+l<=n and y+l<=n:
        re(x,y,l//2)
        re(x,y+l//2,l//2)
        re(x+l//2,y,l//2)
        re(x+l//2,y+l//2,l//2)
    else:
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
            return 0
        elif count1 == l*l:
            return 1
        else:
            return temp

        


answer = re(0,0,n)

print(answer)