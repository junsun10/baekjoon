# 수 찾기 ( 정답 )
# 알고리즘 : 딕셔너리
# 딕셔너리에 저장해 탐색 시간 줄임
# 문제 의도 이분탐색

n = int(input())
arr = list(map(int, input().split()))
dict = {}
for i in arr:
    dict[i] = i
m = int(input())
find = list(map(int, input().split()))
for i in find:
    if i in dict:
        print(1)
    else:
        print(0)
