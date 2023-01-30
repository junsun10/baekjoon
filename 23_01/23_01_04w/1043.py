# 거짓말 ( 정답 )
# 알고리즘 : 그래프, 분리 집합
# 문제 의도는 그래프와 집합을 이용

n, m = map(int, input().split())
arr = list(map(int, input().split()))
if len(arr) == 1:
    c = 0
else:
    c = len(arr) - 1
    arr = arr[1:]
parties = []
for _ in range(m):
    parties.append(list(map(int, input().split())))

answer = 0
visited = [False for _ in range(n+1)]
temp_lie = []

# 진실을 아는 사람이 없는 파티를 파티 별로 temp_lie에 저장
for party in parties:
    temp = []
    for i in range(1, len(party)):
        if party[i] in arr:
            for j in range(1, len(party)):
                visited[party[j]] = True
                temp = []
            break
        elif visited[party[i]]:
            for j in range(1, len(party)):
                visited[party[j]] = True
                temp = []
            break
        else:
            temp.append(party[i])
    if len(temp) > 0:
        temp_lie.append(temp)

# tmep_lie에 진실을 들은 사람이 있으면 해당 파티 제거
while True:
    count = len(temp_lie)
    temp = []
    for lie in temp_lie:
        temp.append(lie)
        for i in range(len(lie)):
            if visited[lie[i]]:
                temp = temp[:-1]
                count -= 1
                for j in range(len(lie)):
                    visited[lie[j]] = True
                break
    # 제거되는 파티가 없으면 중단
    if count == len(temp_lie):
        break
    else:
        temp_lie = temp[:]

print(len(temp_lie))
