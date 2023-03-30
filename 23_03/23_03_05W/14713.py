# 앵무새 ( 정답 )
# 알고리즘 : 구현, 큐
# 받아 적은 문장 L의 단어의 개수가 각 앵무새가 외운 단어의 개수의 합과 같아야 함

n = int(input())
S = [list(map(str, input().split())) for _ in range(n)]
answer = list(map(str, input().split()))
indexes = [0 for _ in range(n)]
end = [False for _ in range(n)]
available = True

if len(answer) != sum(len(s) for s in S):
    available = False
else:
    for word in answer:
        find = False
        for s, index in enumerate(indexes):
            if S[s][index] == word and not end[s]:
                if index + 1 < len(S[s]):
                    indexes[s] += 1
                else:
                    end[s] = True
                find = True
                break
        if not find:
            available = False
            break

print("Possible" if available else "Impossible")
