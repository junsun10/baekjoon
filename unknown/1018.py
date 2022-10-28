row, column = map(int, input().split())

inputboard = []
iandj=[]
change = []

for i in range(row):
    inputboard.append(list(input()))

answer1 = [['W','B','W','B','W','B','W','B'],
           ['B','W','B','W','B','W','B','W'],
           ['W','B','W','B','W','B','W','B'],
           ['B','W','B','W','B','W','B','W'],
           ['W','B','W','B','W','B','W','B'],
           ['B','W','B','W','B','W','B','W'],
           ['W','B','W','B','W','B','W','B'],
           ['B','W','B','W','B','W','B','W']]

answer2 = [['B','W','B','W','B','W','B','W'],
           ['W','B','W','B','W','B','W','B'],
           ['B','W','B','W','B','W','B','W'],
           ['W','B','W','B','W','B','W','B'],
           ['B','W','B','W','B','W','B','W'],
           ['W','B','W','B','W','B','W','B'],
           ['B','W','B','W','B','W','B','W'],
           ['W','B','W','B','W','B','W','B']]

for i in range(0,row-7):
    for j in range(0,column-7):
        iandj.append([i,j])

for i in range(len(iandj)):
    count=0
    for x in range(8):
        for y in range(8):
            if answer1[x][y] != inputboard[x+iandj[i][0]][y+iandj[i][1]]:
                count+=1

    change.append(count)

for i in range(len(iandj)):
    count=0
    for x in range(8):
        for y in range(8):
            if answer2[x][y] != inputboard[x+iandj[i][0]][y+iandj[i][1]]:
                count+=1

    change.append(count)

print(min(change))