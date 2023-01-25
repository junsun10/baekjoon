# 숫자 카드 2 ( 정답 )
# 알고리즘 : 딕셔너리
# 딕셔너리에 카드 숫자를 키, 개수를 값으로 저장

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
finds = list(map(int, input().split()))

count = {}
for i in cards:
    if i not in count.keys():
        count[i] = 1
    else:
        count[i] += 1

for i in finds:
    if i not in count.keys():
        print(0, end=" ")
    else:
        print(count[i], end=" ")
print()
