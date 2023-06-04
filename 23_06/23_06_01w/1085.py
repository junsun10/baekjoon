# 직사격형에서 탈출 ( 정답 )
# 알고리즘 : 수학

x, y, w, h = map(int, input().split())

print(min(x, y, w-x, h-y))
