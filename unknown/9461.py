def triangle(n):
    if (n==1):
        d[1]=1
        return d[1]
    elif (n==2):
        d[2]=1
        return d[2]
    elif (n==3):
        d[3]=1
        return d[3]
    elif (n==4):
        d[4]=2
        return d[4]
    elif (n==5):
        d[5]=2
        return d[5]
    elif (d[n] != 0):
        return d[n]
    else:   # 규칙 : n=6 부터 n-1 + n-5
        d[n] = triangle(n-1) + triangle(n-5)
        return d[n]

t = int(input())
input_n = []
answer=[]

for i in range(t):
    input_n.append(int(input()))

for i in range(len(input_n)):
    d = [0 for _ in range(input_n[i]+1)]
    triangle(input_n[i])
    answer.append(d[input_n[i]])

for i in answer:
    print(i)
    