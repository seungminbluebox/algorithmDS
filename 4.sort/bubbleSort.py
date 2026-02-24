def bubbleSort(arr):
    n=len(arr)
    for j in range(n-1):
        swap=False
        for i in range(n-1-j):

            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swap=True
        if swap==False:
            break
    return arr
arr=[5,32,4,8,3,2,4]
print(bubbleSort(arr))