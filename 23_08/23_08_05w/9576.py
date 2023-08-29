# 책 나눠주기 ( 알고리즘 확인, 정답 확인 )
# 알고리즘: 그리디
# 시작 지점이 아닌 끝 지점을 기준으로 정렬한 뒤 그리디

for _ in range(int(input())):
    n, m = map(int, input().split())
    book = [False for _ in range(n+1)]
    arr = []
    for _ in range(m):
        a, b = map(int, input().split())
        arr.append([a, b])

    # 끝 지점 기준으로 정렬
    arr.sort(key=lambda x: x[1])

    # 그리디
    count = 0
    for a, b in arr:
        for i in range(a, b+1):
            if book[i] == False:
                book[i] = True
                count += 1
                break

    print(count)
