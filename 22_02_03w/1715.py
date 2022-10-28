# 카드 정렬하기 ( 틀림 )
# 


import sys

# N 입력
n = int(sys.stdin.readline())

# 카드 입력
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

sum=0
arr.sort()
while len(arr)>1:
    temp=[]
    if len(arr)%2==0:
        for i in range(0,len(arr),2):
            temp.append(arr[i]+arr[i+1])
            sum = sum + arr[i] + arr[i+1]
    else:
        for i in range(0,len(arr)-1,2):
            temp.append(arr[i]+arr[i+1])
            sum = sum + arr[i] + arr[i+1]
        sum = sum + temp[0] + arr[-1]
        temp[0] += arr[-1]
    arr = temp

print(sum)