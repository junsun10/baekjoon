# 공유기 설치 ( 알고리즘 확인, 알고리즘 검색 )
# 알고리즘: 이분 탐색
# 가장 인접한 두 공유기 사이의 거리를 이분 탐색으로 구함

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

start = 0
end = house[-1] - house[0]
answer = 0

while True:
    if start > end:
        break

    d = (end+start)//2

    count = 1
    # 마지막으로 공유기 설치된 집 인덱스
    before = 0

    for i in range(1, n):
        if house[i] - house[before] >= d:
            before = i
            count += 1

        else:
            continue

    if count >= c:
        start = d+1
        answer = d
    else:
        end = d-1

print(answer)
