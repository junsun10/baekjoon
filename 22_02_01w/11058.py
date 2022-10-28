# 크리보드 ( 정답 )

n = int(input())

d=[0 for _ in range(101)]

# def kriii(x):
#     if x==1:
#         d[1]=1
#         return d[1]
#     if x==2:
#         d[2]=2
#         return d[2]
#     if x==3:
#         d[3]=3
#         return d[3]
#     if x==4:
#         d[4]=4
#         return d[4]
#     if x==5:
#         d[5]=5
#         return d[5]
#     if x==6:
#         d[6]=6
#         return d[6]
#     if x==7:
#         d[7]=9
#         return d[7]
#     if x==8:
#         d[8]=12
#         return d[8]
#     if x==9:
#         d[9]=15
#         return d[9]
#     if x==10:
#         d[10]=18
#         return d[10]

#     if d[x] != 0:
#         return d[x]
    
#     else:
#         if (x-10)%4==1:
#             d[x] = kriii(x-4)*3
#             return d[x]
#         else:
#             d[x] = kriii(x-5)*4
#             return d[x]

# kriii(n)



def kriii(x):

    # 1~6까지는 A만 출력

    if x==0:
        return d[0]
    elif x==1:
        d[1]=1
        return d[1]
    elif x==2:
        d[2]=2
        return d[2]
    elif x==3:
        d[3]=3
        return d[3]
    elif x==4:
        d[4]=4
        return d[4]
    elif x==5:
        d[5]=5
        return d[5]
    elif x==6:
        d[6]=6
        return d[6]

    # dp
    elif d[x] != 0:
        return d[x]


    # 자신보다 3개 앞 출력 횟수를 2배한 것
    # (한번 붙여넣는데 최소 세번의 횟수가 들기때문)

    # 자신보다 4개 앞 출력 횟수를 3배한 것
    # .
    # .
    # .
    # x 보다 x-1개 앞 출력 횟수를 (x-1-1)배한 것
    # 중 최댓값 선택
    
    else:
        arr=[]
        for i in range(3,x):
            arr.append((kriii(x-i))*(i-1))
        # print(arr)
        d[x] = max(arr)
        return d[x]
            

kriii(n)
print(d[n])
