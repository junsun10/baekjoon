# 단어 정렬 ( 정답 )
# 알고리즘: 문자열, 정렬

n = int(input())
arr = [input() for _ in range(n)]

arr.sort()

arr.sort(key=lambda x: len(x))

temp = arr[0]
print(arr[0])
for i in range(1, n):
    if temp == arr[i]:
        continue
    else:
        temp = arr[i]
        print(arr[i])
