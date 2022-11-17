# 연결 요소의 개수 ( 정답 )
# 알고리즘 : 완전탐색
# 그룹에 있는지 확인한 뒤 추가

n, m = map(int, input().split())
mArr = [list(map(int, input().split())) for _ in range(m)]
mArr.sort()
groups = []
visited = [False for _ in range(n+1)]

for x, y in mArr:
    find = False
    for group in groups:
        if x in group or y in group:
            find = True
        if x in group and y not in group:
            group.append(y)
            find = True
            visited[y] = True
            break
        elif y in group and x not in group:
            group.append(x)
            find = True
            visited[x] = True
            break
        else:
            continue
    if not find:
        groups.append([x, y])
        visited[x] = True
        visited[y] = True

count = 0
for i in range(1, n+1):
    if visited[i] == False:
        count += 1

print(len(groups)+count)
