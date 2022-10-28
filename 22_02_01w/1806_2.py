# 부분합 ( 정답 )

import sys

# N,S 입력
n,s = map(int,sys.stdin.readline().split())

# 배열 입력
arr=list(map(int,sys.stdin.readline().split()))

# 시작, 끝 인덱스
# 정답 길이, sum
start=0
end=0
answer=100000
sum=0

# 첫번째 숫자 더하고 시작
sum += arr[0]

# 시작이 n 넘기 전까지 반복
while(start!=n):
    # print("start: ",start," end: ",end)
    # print(sum)

    # sum이 s보다 크거나같으면 길이를 구하고
    # 그것이 answer보다 작으면 할당
    # 그리고 시작 인덱스 + 1
    if sum >= s:
        if answer > end - start + 1:
            answer = end - start + 1
        # print(start,end,sum,answer)
        sum -= arr[start]
        start += 1

    # sum이 s보다 작으면
    else:
        # 끝 인덱스가 n-1 될때까지만 더해줌
        if end < n-1:
            end += 1
            sum += arr[end]
        # 이미 끝 인덱스가 n-1 이므로
        # 시작 인덱스 늘려서 while탈출 
        else:
            sum -= arr[start]
            start += 1

# 정답이 초깃값 그대로면 불가능
if answer == 100000:
    print(0)
else:
    print(answer)