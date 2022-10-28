

def fibonacci(n):
    if (n==0):
        d[0]=0
        global c0
        c0 = c0 + 1
        e[0]=[1,0]
        return d[0]
    elif (n==1):
        d[1]=1
        global c1
        c1 = c1 + 1
        e[1]=[0,1]
        return d[1]
    elif (d[n] != 0):
        c0=c0+e[n][0]
        c1=c1+e[n][1]
        return d[n]
    else:
        d[n] = fibonacci(n-1)+fibonacci(n-2)
        e[n] = [c0,c1]
        return d[n]

t = int(input())
input_n = []

for i in range(t):
    input_n.append(int(input()))

for i in range(len(input_n)):
    d = [0 for _ in range(input_n[i]+1)]
    e = [0 for _ in range(input_n[i]+1)]
    c0=0
    c1=0
    fibonacci(input_n[i])
    for j in range(2):
        print(e[input_n[i]][j],end=" ")
    print()

