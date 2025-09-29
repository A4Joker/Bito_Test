def findMedian(arr):
    #n = int(input())
    #array = list(map(int,input().split()))[:n]
    mid = int()
    sorted_arr = sorted(arr)
    print(sorted_arr)
    if len(sorted_arr) % 2 != 0:
        mid = len(sorted_arr) // 2
    print(sorted_arr[mid])
    


findMedian([0,1,4,2,3])

#findMedian([0,1,4,2,3])