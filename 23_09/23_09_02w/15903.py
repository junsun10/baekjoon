# 카드 합체 놀이 ( 정답 )
# 알고리즘: 그리디, 힙
# 정렬 대신 최소힙을 사용해 시간 줄일 수 있음

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for _ in range(m):
    temp = arr[0] + arr[1]
    arr[0] = temp
    arr[1] = temp
    arr.sort()

print(sum(arr))
