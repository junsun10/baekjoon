
n,m = input().split()
n = int(n)
m = int(m)

list = []
list = input().split()
for i in range(len(list)):
    list[i] = int(list[i])


answer = 0
sum = 0

for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum = list[i]+list[j]+list[k]
            if sum <= m and sum > answer:
                answer = sum
                sum = 0

print(answer)