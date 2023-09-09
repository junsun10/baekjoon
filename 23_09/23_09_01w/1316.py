# 그룹 단어 체커 ( 정답 )
# 알고리즘: 구현

n = int(input())

answer = 0

for _ in range(n):
    failed = False
    visited = []
    str = input()

    for index, value in enumerate(str):
        if value not in visited:
            visited.append(value)
        else:
            if str[index-1] == value:
                continue
            else:
                failed = True
                break

    if not failed:
        answer += 1

print(answer)
