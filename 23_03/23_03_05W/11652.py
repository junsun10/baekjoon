# 카드 ( 정답 )
# 알고리즘 : 해시, 딕셔너리

import sys

n = int(sys.stdin.readline())
max_card = [0, 0]  # index, count
cards = dict()
for i in range(n):
    card = int(sys.stdin.readline())
    if card not in cards:
        cards[card] = 1
    else:
        cards[card] = cards[card] + 1

for key, value in cards.items():
    if value == max_card[1] and key < max_card[0]:
        max_card[0] = key
    elif value > max_card[1]:
        max_card[0] = key
        max_card[1] = value
    else:
        continue

print(max_card[0])
