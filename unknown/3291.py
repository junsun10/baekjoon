# LIST

n = int(input())
songs = []
list = ["" for _ in range(n)]
answer = []

for i in range(n):
    name = input()
    state = input()
    if state == "UP":
        songs.append([n-i-1] + [name] + [j for j in range(i+1, n)])
    elif state == "DOWN":
        songs.append([i] + [name] + [j for j in range(0, i)])
    else:
        songs.append([1] + [name] + [i])


def dfs(x):
    global answer
    print(list)
    if len(answer) > 0:
        return

    if x == n:
        answer = list[:]
        return

    for i in range(2, len(songs[x])):
        if list[songs[x][i]] == "":
            list[songs[x][i]] = songs[x][1]
            dfs(x+1)
            list[songs[x][i]] = ""


print(songs)
songs.sort()
print(songs)
dfs(0)
for i in answer:
    print(i)
