# 비밀번호 ( 정답 )
# 알고리즘: dp
# dict를 통해 각 숫자에서 이어질 수 있는 번호 저장
# count를 통해 현재까지 비밀번호 경우의 수에서 마지막 숫자 별 개수 저장
# 해당 숫자에서 이어질 수 있는 번호를 count값 만큼 더함

dict = {1: [2, 4], 2: [1, 3, 5], 3: [2, 6], 4: [1, 5, 7],
        5: [2, 4, 6, 8], 6: [3, 5, 9], 7: [4, 8, 0], 8: [5, 7, 9], 9: [6, 8], 0: [7]}

for _ in range(int(input())):
    n = int(input())
    # 비밀번호 길이가 1인 상태
    count = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 0: 1}
    for i in range(n-1):
        # new_count 초기화
        new_count = {}
        for j in range(10):
            new_count[j] = 0

        # count 0부터 9까지
        for j in range(10):
            # 마지막 자리가 j인 경우의 수
            temp = count[j]

            # j에서 이어질 수 있는 번호 k
            for k in dict[j]:
                new_count[k] += 1*temp
                new_count[k] %= 1234567

        count = new_count.copy()

    answer = 0
    for i in range(10):
        answer += count[i]
        answer %= 1234567
    print(answer)
