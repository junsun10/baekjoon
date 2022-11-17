# 쿼드트리 ( 구글정답 )

import sys
input = sys.stdin.readline
limit_number = 10000
sys.setrecursionlimit(limit_number)

n = int(input())
in_arr = [list(map(int,input().strip())) for _ in range(n)]
answer = []

def re(x,y,l):
    global answer

    cheak = in_arr[x][y]
    for i in range(x,x+l,1):
        for j in range(y,y+l,1):
            if in_arr[i][j] != cheak:
                print("(",end="")
                re(x,y,l//2)
                re(x,y+l//2,l//2)
                re(x+l//2,y,l//2)
                re(x+l//2,y+l//2,l//2)
                print(")",end="")
                return

    if cheak == 0:
        print("0",end="")
        return
    else:
        print("1",end="")
        return

        


re(0,0,n)
print()
