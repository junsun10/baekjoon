# 숨바꼭질 ( 시간초과 )

# 전체 경우의수 한 배열에 더해나가는 방식

import sys

# N,K 입력
n,k = map(int,sys.stdin.readline().split())

# 경우의수 +1, -1, *2

endprg = False
val=[]
val.append(n)
index=0
second=0

if n==k:
    print(0)
else:
    while True:
        second += 1
        for i in range(3**(second-1)):
            val.append(val[index+i]+1)
            val.append(val[index+i]-1)
            val.append(val[index+i]*2)
            if k in val:
                endprg = True
                break
        index = index+3**(second-1)
        if endprg:
            print(second)
            break

