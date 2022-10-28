n = input()
length = len(n)
n = int(n)
list=[]

sum=0

for i in range(1,n):
    temp=i
    sum=i
    while(1):
        sum = sum + temp%10
        temp=(temp-temp%10)/10
        if temp<1:
            break
    if sum == n:
        list.append(i)

if len(list)==0:
    print(0)
else:
    print(min(list))



