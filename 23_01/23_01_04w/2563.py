# 색종이 ( 정답 )
# 알고리즘 : 구현

arr = [[0 for _ in range(101)] for _ in range(101)]
t = int(input())
answer = 0

for _ in range(t):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            if arr[x+i][y+j] == 0:
                answer += 1
                arr[x+i][y+j] = 1

print(answer)
