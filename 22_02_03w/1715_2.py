# 카드 정렬하기 ( 틀림 )
# 


import sys

# N 입력
n = int(sys.stdin.readline())

# 카드 입력
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))


sum=sum(arr)
arr.sort()
answer = 0
while True:
    temp=0

    for i in range(len(arr)):
        if temp + arr[i] <= sum//2:
            if i == 0:
                temp = temp + arr[i]
            else:
                answer = answer + temp + arr[i]
                temp = temp + arr[i]
            # print(answer, temp)
        else:
            arr = arr[i:]
            arr.append(temp)
            break
    # print(arr)
    # print(answer)
    # print()
    if len(arr)<=3:
        break
    
if len(arr) == 3:
    answer = answer + arr[0]*2 + arr[1]*2 + arr[2]
    print(answer)
else:
    answer = answer + arr[0] + arr[1]
    print(answer)