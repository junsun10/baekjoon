# LIST

n = int(input())
songs_up = []
songs_down = []
list = ["" for _ in range(n)]

for i in range(n):
    name = input()
    state = input()
    if state == "UP":
        songs_up.append([name] + [j for j in range(i+1, n)])
    elif state == "DOWN":
        songs_down.append([name] + [j for j in range(0, i)])
    else:
        list[i] = name

index = 0
for i in range(len(songs_down)):
    # print(list)
    while True:
        if list[index] != "":
            index += 1
        else:
            break

    for j in range(1, len(songs_down[i])):
        if songs_down[i][j] == index:
            list[index] = songs_down[i][0]
            index += 1
            break

index = n-1
for i in range(len(songs_up)-1, -1, -1):
    # print(list)
    while True:
        if list[index] != "":
            index -= 1
        else:
            break

    for j in range(1, len(songs_up[i])):
        if songs_up[i][j] == index:
            list[index] = songs_up[i][0]
            index -= 1
            break


for i in list:
    print(i, end="\n")
