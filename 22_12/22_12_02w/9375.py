# 패션왕 신해빈 ( 정답 )
# 알고리즘 : 딕셔너리, 조합
# 옷의 종류에 따라 딕셔너리 자료구조에 저장
# 입을 수 있는 옷의 조합 계산


for _ in range(int(input())):
    answer = 0
    n = int(input())
    dic = dict()
    for _ in range(n):
        name, category = map(str, input().split())
        if category in dic:
            temp = dic[category]
            temp.append(name)
            dic[category] = temp
        else:
            dic[category] = [name]

    if len(dic) == 1:
        print(n)
    else:
        temp = 1
        for i in dic:
            temp *= len(dic[i])+1
        answer += temp
        print(answer-1)
