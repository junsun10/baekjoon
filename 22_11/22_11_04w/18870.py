# 좌표 압축 ( 시간초과 )

n = int(input())
arr = list(map(int, input().split()))
newArr = []
answer = [0 for _ in range(n)]

for i in range(n):
    newArr.append([arr[i], i])

newArr.sort()

for i in range(n):
    answer[newArr[i][1]] += i
    if i > 0 and newArr[i-1][0] == newArr[i][0]:
        for k in range(i, n, 1):
            answer[newArr[k][1]] -= 1

for i in answer:
    print(i, end=" ")
print()
