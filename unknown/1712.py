a,b,c = map(int,input().split())

# print(a,b,c)

if b >= c:
    print(-1)

else:
    n = a//(c-b)
    print(n+1)