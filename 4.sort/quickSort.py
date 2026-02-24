def quickSort(arr,low,high):
    if low<high:
        p=partition(arr,low,high)
        quickSort(arr,low,p-1)
        quickSort(arr,p+1,high)
    return arr

def partition(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if pivot>arr[j]:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    arr[high],arr[i+1]=arr[i+1],arr[high]
    return i+1

arr=[5,3,21,8,3,2,4,5]
print(quickSort(arr,0,len(arr)-1))