# N과 M (9) ( 정답, 알고리즘 검색 )
# 알고리즘 : 백트래킹
# 한번 출력된 수열을 딕셔너리에 넣어 반복 출력되지 않게 함
# 배열에 넣어서 in 사용했을 때 시간초과

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
answers = {}
answer = []
visited = [False for _ in range(n)]


def dfs():
    for i in range(len(nums)):
        if len(answer) == m and answers.get(str(answer)) == None:
            answers[str(answer)] = True
            print(" ".join(map(str, answer)))
            return

        if not visited[i]:
            answer.append(nums[i])
            visited[i] = True
            dfs()
            answer.pop()
            visited[i] = False


dfs()
