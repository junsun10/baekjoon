d=[[0 for _ in range(501)] for _ in range(501)]

n = int(input())

for i in range(1,n+1):
    triangle = list(map(int,input().split()))
    x = len(triangle)
    for j in range(1,x+1):
        if j == 1:
            d[i][j] = d[i-1][j] + triangle[j-1]
        elif j == x:
            d[i][j] = d[i-1][j-1] + triangle[j-1]
        else:
            d[i][j] = max(d[i-1][j-1], d[i-1][j]) + triangle[j-1]    
    

print(max(d[n]))

    
        