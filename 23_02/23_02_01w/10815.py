# 숫자 카드 ( 정답 )
# 알고리즘 : 이분탐색

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
arr.sort()


for i in arr2:
    isin = False
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start + end)//2

        if i == arr[mid]:
            print(1, end=" ")
            isin = True
            break
        elif i > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    if not isin:
        print(0, end=" ")
print()
