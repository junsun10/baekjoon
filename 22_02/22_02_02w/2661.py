# 좋은수열 ( 정답 )
# 현재 수열에서 1,2,3 순서대로 더했을 때 좋은 수열이면 더하는 함수 만듬
# 모두 나쁜수열이면 마지막수를 지우고 함수에 넣음 대신 지우기 전 수열을 저장해서
# 똑같은 수열로 만들지 않도록 함

import sys

# N 입력
n = int(sys.stdin.readline())

# 좋은 수열인지 판단
def good(array):
    isgood = True
    for i in range(1,len(array)//2+1):
        # print("i:",i)
        for j in range(len(array)-2*i+1):
            # print("j:",j)
            # print(array[j:j+i])
            # print(array[j+i:j+i+i])
            if array[j:j+i]==array[j+i:j+i+i]:
                isgood = False
                break
        if not isgood:
            break
    return isgood
    

# 수열 더하는 함수
def addnumber(array, before):

    # 가장 작은 수를 만들어야 하므로 1,2,3 순서
    if good(array + "1") and not(array + "1" == before):
        array += "1"
        return array, before
    elif good(array + "2") and not(array + "2"== before):
        array += "2"
        return array, before
    elif good(array + "3") and not(array + "3"== before):
        array += "3"
        return array , before
    
    # 1,2,3 모두 불가능하면 한자리 삭제
    else:
        before = array
        array = array[:-1]
        return addnumber(array, before)


# 정답 수열 저장
arr = ""
# 삭제하기 이전 배열 저장
bef = ""


# 수열 길이가 n 일때까지
while len(arr) < n:
    arr, bef = addnumber(arr,bef)

print(arr)


