n = int(input())

cost = []
for i in range(n):
    cost.append(list(map(int,input().split())))

d1 = [0]*1001
d2 = [0]*1001
d3 = [0]*1001
index = [0]*1001

# (1,1) 선택
d1[0]=cost[0][0]
index[0]=0
for i in range(1,n):
    if index[i-1]==0:
        if cost[i][1] < cost[i][2]:
            index[i]=1
            d1[i]=d1[i-1]+cost[i][1]
        else:
            index[i]=2
            d1[i]=d1[i-1]+cost[i][2]
    elif index[i-1]==1:
        if cost[i][0] < cost[i][2]:
            index[i]=0
            d1[i]=d1[i-1]+cost[i][0]
        else:
            index[i]=2
            d1[i]=d1[i-1]+cost[i][2]
    else:
        if cost[i][0] < cost[i][1]:
            index[i]=0
            d1[i]=d1[i-1]+cost[i][0]
        else:
            index[i]=1
            d1[i]=d1[i-1]+cost[i][1]

# (1,2) 선택
index = [0]*1001
d2[0]=cost[0][1]
index[0]=1
for i in range(1,n):
    if index[i-1]==0:
        if cost[i][1] < cost[i][2]:
            index[i]=1
            d2[i]=d2[i-1]+cost[i][1]
        else:
            index[i]=2
            d2[i]=d2[i-1]+cost[i][2]
    elif index[i-1]==1:
        if cost[i][0] < cost[i][2]:
            index[i]=0
            d2[i]=d2[i-1]+cost[i][0]
        else:
            index[i]=2
            d2[i]=d2[i-1]+cost[i][2]
    else:
        if cost[i][0] < cost[i][1]:
            index[i]=0
            d2[i]=d2[i-1]+cost[i][0]
        else:
            index[i]=1
            d2[i]=d2[i-1]+cost[i][1]

# (1,3) 선택
index = [0]*1001
d3[0]=cost[0][2]
index[0]=2
for i in range(1,n):
    if index[i-1]==0:
        if cost[i][1] < cost[i][2]:
            index[i]=1
            d3[i]=d3[i-1]+cost[i][1]
        else:
            index[i]=2
            d3[i]=d3[i-1]+cost[i][2]
    elif index[i-1]==1:
        if cost[i][0] < cost[i][2]:
            index[i]=0
            d3[i]=d3[i-1]+cost[i][0]
        else:
            index[i]=2
            d3[i]=d3[i-1]+cost[i][2]
    else:
        if cost[i][0] < cost[i][1]:
            index[i]=0
            d3[i]=d3[i-1]+cost[i][0]
        else:
            index[i]=1
            d3[i]=d3[i-1]+cost[i][1]

print(d1[n-1])
print(d2[n-1])
print(d3[n-1])
print(min(d1[n-1],d2[n-1],d3[n-1]))

# 순간의 최소를 선택한것이 최종 최소가 아님
# 어떻게 해결?