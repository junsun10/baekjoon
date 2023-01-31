# 커트라인 ( 정답 )
# 알고리즘 : 구현, 정렬

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(arr[-k])
