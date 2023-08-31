# 두 용액 ( 정답 )
# 알고리즘: 두 포인터, 이분 탐색
# 입력 숫자를 정렬한 뒤 양 끝에서부터 최솟값 탐색

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

answer = 2000000000
answer_list = []
i,j = 0,n-1
while i < j:
    temp = arr[i] + arr[j]

    if abs(temp) < answer:
        answer = abs(temp)
        answer_list = [arr[i],arr[j]]

    if temp > 0:
        j -= 1
    elif temp < 0:
        i += 1
    else:
        break


print(*answer_list)


