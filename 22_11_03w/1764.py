# 듣보잡 ( 정답 )
# 알고리즘 : 딕셔너리
# 딕셔너리를 사용해 탐색 시간 줄임
# set도 사용 가능

n, m = map(int, input().split())
nArr = dict()
answer = []

for _ in range(n):
    nArr[input()] = 0
for _ in range(m):
    name = input()
    if nArr.get(name) == 0:
        answer.append(name)

print(len(answer))
answer.sort()
for name in answer:
    print(name)
