# 문자열 집합 ( 정답 )
# 알고리즘 : 딕셔너리
# 딕셔너리에 문자열 집합 추가해준 뒤
# 검사할 문자열이 딕셔너리에 있는지 확인

n, m = map(int, input().split())
s = {}
for i in range(n):
    t = input()
    s[t] = 1
answer = 0

for _ in range(m):
    t = input()
    if s.get(t, 0) == 1:
        answer += 1

print(answer)
