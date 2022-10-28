#피보나치 동적계획
answer = []

def fibonacci(n):
    if (n==0):
        d[0]=0
        return d[0]
    elif (n==1):
        d[1]=1
        return d[1]
    elif (d[n] != 0):
        return d[n]
    else:
        d[n] = fibonacci(n-1)+fibonacci(n-2)
        return d[n]

t = int(input())
input_n = []

for i in range(t):
    input_n.append(int(input()))

print(input_n)

for i in range(len(input_n)):
    d = [0 for j in range(input_n[i]+1)]
    print(d)
    answer.append(fibonacci(input_n[i]))
    print(d)


for i in answer:
    print(i)



