def selectSort(arr):
    n=len(arr)
    for j in range(n):
        minIndex=j
        for i in range(j,n):
            if arr[minIndex]>arr[i]:
                minIndex=i
        arr[j],arr[minIndex]=arr[minIndex],arr[j]
    return arr

arr=[5,63,1]
print(selectSort(arr))