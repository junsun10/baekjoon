# 좌표 압축 ( 정답 )
# 알고리즘 : 정렬, 구현
# 입력받은 배열의 인덱스를 추가해준 뒤 정렬
# 같은 값이 여러번 나오면 temp에 개수를 누적해서
# 정렬된 인덱스값에서 빼줌
# 원래 출제의도는 set, dict를 쓰는것


n = int(input())
arr = list(map(int, input().split()))
newArr = []
answer = [0 for _ in range(n)]

for i in range(n):
    newArr.append([arr[i], i])

newArr.sort()

temp = 0
for i in range(n):
    answer[newArr[i][1]] += i
    if i > 0 and newArr[i-1][0] == newArr[i][0]:
        temp -= 1
    answer[newArr[i][1]] += temp


for i in answer:
    print(i, end=" ")
print()
