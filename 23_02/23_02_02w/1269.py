# 대칭 차집합 ( 정답 )
# 알고리즘 : 집합

la, lb = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sa = set(a)
sb = set(b)

answer = len(sa-sb)
answer += len(sb-sa)
print(answer)
