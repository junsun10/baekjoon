# 신입 사원 ( 정답 )
# 알고리즘 : 정렬, 그리디
# 한쪽 성적 순위를 먼저 정렬한 뒤
# 앞에서부터 두번째 성적 순위가 현재 최고 등수보다 높은지 낮은지 확인

for _ in range(int(input())):
    answer = 0
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_val = n+1

    arr.sort()

    for i in range(n):
        if arr[i][1] > min_val:
            continue
        else:
            answer += 1
            min_val = arr[i][1]

    print(answer)
