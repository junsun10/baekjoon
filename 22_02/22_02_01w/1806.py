# 부분합 ( 시간초과 )

import sys

# N,S 입력
n,s = map(int,sys.stdin.readline().split())

# 배열 입력
arr=list(map(int,sys.stdin.readline().split()))

# 불가능한 경우 계산
temp=0
for i in range(n):
    temp += arr[i]

# 불가능한 경우
if temp < s:
    print(0)

# 최소길이를 1부터 1씩 더해가며 계산
# sum을 처음 계산한 이후 다음 sum 계산할 때 
# 앞에서 하나 빼고 뒤에서 하나 더하면서 계산

else:
    for i in range(1,n+1):
        endprg = False
        sum=0

        # 처음 sum 계산
        for k in range(0,i):
            sum += arr[k]
        
        # print("i:",i)
        # print("sum1: ",sum)

        if sum >= s:
            print(i)
            break
        
        # 앞에서 하나 빼고 뒤에서 하나 더함
        for j in range(1,n-i+1):

            sum = sum - arr[j-1] + arr[j+i-1]
            # print("arr[j-1]:",arr[j-1])
            # print("arr[j+i-1]",arr[j+i-1])
            # print("sum: ",sum)
            # print()
            
            if sum >= s:
                print(i)
                endprg = True
                break

        if endprg == True:
            break

            


        