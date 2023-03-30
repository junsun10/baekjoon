# 국회의원 선거 ( 정답 )
# 알고리즘 : 구현

n = int(input())
votes = [int(input()) for _ in range(n)]
max_length = max(votes)
answer = 0
end = False

if n == 1:
    print(0)
else:
    while not end:
        for i in range(1, n):
            if votes[i] == max_length:
                votes[i] -= 1
                votes[0] += 1
                answer += 1

            if max(votes) == votes[0]:
                temp = 0
                for j in votes:
                    if max(votes) == j:
                        temp += 1
                if temp == 1:
                    end = True
                    break
        max_length -= 1

    print(answer)
