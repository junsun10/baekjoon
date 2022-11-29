# Z ( 정답 )
# 알고리즘 : 재귀, 분할정복
# 전체 배열에서 몇사분면에 있는지 재귀적으로 탐색후 배열에 저장
# 저장한 배열로 몇번째 탐색인지 계산

n, x, y = map(int, input().split())
temp = n
arr = []

while temp > 0:
    if 2**(temp-1) > x and 2**(temp-1) > y:
        arr.append([1, temp])
    elif 2**(temp-1) > x and 2**(temp-1) <= y:
        arr.append([2, temp])
        y -= 2**(temp-1)
    elif 2**(temp-1) <= x and 2**(temp-1) > y:
        arr.append([3, temp])
        x -= 2**(temp-1)
    else:
        arr.append([4, temp])
        x -= 2**(temp-1)
        y -= 2**(temp-1)
    temp -= 1

answer = 0
for i, n in arr:
    if i == 1:
        continue
    elif i == 2:
        answer += 4**(n-1)
    elif i == 3:
        answer += (4**(n-1))*2
    else:
        answer += (4**(n-1))*3

print(answer)
