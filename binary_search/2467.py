n = int(input())
arr = map(int, input().split())

min_sum = 2000000000
min_sum_val = []

for i in range(n):
    temp = arr[i]
    start = 0
    end = n-1
    mid = (start+end)//2
    mid_val = arr[mid]
    # while True:
    #     if end < start:
    #         break


    #     if mid_val + temp > 0:
    #         end = mid
    #         if mid_val + temp < abs(min_sum)
    #     elif mid_val + temp < 0:
    #         start = mid
    #     elif mid_val + temp == 0:
    #         print(temp,mid_val)
    #         return 0
