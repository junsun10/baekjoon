i=666
answer=[]

N = int(input())

# while(len(answer)!=N):
#     count=0
#     temp = str(i)
#     for j in range(len(temp)):
#         if temp[j]=='6':
#             count+=1
#         else:
#             count=0
        
#         if count == 3:
#             answer.append(i)
#             break
    
#     i+=1

a='666'
while(len(answer)!=N):
    count=0
    temp = str(i)
    if a in temp:
        answer.append(i)
    
    i+=1

# 둘다정답

print(answer[N-1])