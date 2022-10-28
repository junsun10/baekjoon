# 접미사 배열 ( 정답 )

import sys

word = sys.stdin.readline()

new_word = []

for i in range(len(word)-1):
    temp = word[i:-1]
    new_word.append(temp)

new_word.sort()
for i in new_word:
    print(i)