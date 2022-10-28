N = int(input())

list = [[0]*2 for _ in range(N)]
rate = [0 for _ in range(N)]


for i in range(N):
    list[i][0], list[i][1] = map(int, input().split())

for i in range(N):
    for j in range(N):
        if list[i][0] < list[j][0] and list[i][1] < list[j][1]:
            rate[i] = rate[i] + 1
    rate[i] = rate[i] + 1


for i in rate:
    print(i,end=" ")