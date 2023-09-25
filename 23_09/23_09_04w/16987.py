# 계란으로 계란치기 ( 정답 )
# 알고리즘: 백트래킹
# 규칙에 따라 모든 경우의 수를 백트래킹으로 탐색

n = int(input())
arr = []
for _ in range(n):
    s, w = map(int, input().split())
    arr.append([s, w])
status = [True for _ in range(n)]
answer = 0


# 계란으로 계란 치기
def fight(x, y):
    global arr, status
    if arr[x][0] - arr[y][1] <= 0:
        status[x] = False
    else:
        arr[x][0] -= arr[y][1]

    if arr[y][0] - arr[x][1] <= 0:
        status[y] = False
    else:
        arr[y][0] -= arr[x][1]

# 되돌리기


def reverse(x, y):
    global arr, status

    if status[x] == False:
        status[x] = True
    else:
        arr[x][0] += arr[y][1]

    if status[y] == False:
        status[y] = True
    else:
        arr[y][0] += arr[x][1]


def dfs(start):
    global arr, status, answer

    # 마지막까지 완료하면 종료
    if start == n:
        return

    check = 0
    for i in range(n):
        if status[i] == False:
            check += 1

    # 현재 계란이 깨져있거나 깨지지 않은 계란이 없는 경우
    if status[start] == False or check == n:
        dfs(start+1)

    else:
        for i in range(n):
            # 자신과 다른 위치고 깨지지 않은 경우 계란 치기
            if start != i and status[i] != False:
                # 계란 치기
                fight(start, i)

                # 최댓값 저장
                count = 0
                for j in range(n):
                    if status[j] == False:
                        count += 1
                answer = max(answer, count)

                # 다음 순서 진행
                dfs(start+1)
                # 되돌리기
                reverse(start, i)


dfs(0)
print(answer)
