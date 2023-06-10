# 암호 만들기 ( 정답 )
# 알고리즘 : 완전탐색, 조합
# 모음과 자음을 선택하는 개수 전체 탐색
# 개수에 따라 모음과 자음 선택할 수 있는 조합 탐색
# 해당 조합으로 모음과 자음 연결해 정렬
# 전체 경우의 수 정렬해 출력

from itertools import combinations

l, c = map(int, input().split())
alphabets = list(map(str, input().split()))

alphabets.sort()

# 입력에 들어있는 모음, 자음 분리
vowels = []
consonants = []
for alphabet in alphabets:
    if alphabet in ["a", "e", "i", "o", "u"]:
        vowels.append(alphabet)
    else:
        consonants.append(alphabet)

answers = []
# 모음 i개 자음 l-i개 선택
for i in range(1, l-1):
    # 모음 경우의 수
    vowel = combinations(vowels, i)
    vowel_list = []
    for j in vowel:
        vowel_list.append(list(j))

    # 자음 경우의 수
    consonant = combinations(consonants, l-i)
    consonant_list = []
    for j in consonant:
        consonant_list.append(list(j))

    # 모든 경우의수 조합
    for j in vowel_list:
        for k in consonant_list:
            temp = j + k
            temp.sort()
            answers.append(temp)

answers.sort()
for answer in answers:
    print("".join(answer))
