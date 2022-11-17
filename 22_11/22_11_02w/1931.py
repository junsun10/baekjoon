# 회의실 배정 ( 정답 )
# 알고리즘 : 그리디 알고리즘, 정렬
# 회의가 끝나는 시간을 오름차순으로 정렬
# 단 끝나는 시간이 같으면 시작시간이 빠른 순서로 정렬
# 회의가 끝나는 시간이 오름차순으로 정렬되어있으므로
# 앞 회의가 끝나는대로 다음 회의 추가

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
arr.sort(key=lambda x: x[1])
right = 0
answer = 0
for x, y in arr:
    if x >= right:
        right = y
        answer += 1
print(answer)
