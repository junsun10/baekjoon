# 가운데를 말해요 

import sys

# N 입력
n = int(sys.stdin.readline())

arr = []

arr.append(int(sys.stdin.readline()))
print(arr[0])

mid=0
index=0
for i in range(n-1):  
    temp = int(sys.stdin.readline())
    if temp == mid:
        arr.insert(index,temp)
    elif temp > mid:

        for j in range(index,len(arr)):
            # print(temp,arr[j])
            if j==len(arr)-1 and temp > arr[j]:
                # print(arr)
                arr.insert(j+1,temp)
                # print(arr)
                # print()
            if temp < arr[j]:
                # print(arr)
                arr.insert(j,temp)
                # print(arr)
                # print()
                break
    else:
        for j in range(index):
            # print(temp,arr[j])
            if j==len(arr)-1 and temp > arr[j]:
                # print(arr)
                arr.insert(j+1,temp)
                # print(arr)
                # print()
            if temp < arr[j]:
                # print(arr)
                arr.insert(j,temp)
                # print(arr)
                # print()
                break
            
    if len(arr)%2==0:
        print(arr[len(arr)//2-1])
        mid=arr[len(arr)//2-1]
        index=len(arr)//2-1
    else:
        print(arr[len(arr)//2])
        mid=arr[len(arr)//2]
        index=len(arr)//2
