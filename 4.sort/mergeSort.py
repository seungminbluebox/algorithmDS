def mergeSort(arr,left,right):
    if left>=right:
        return
    mid=(left+right)//2
    mergeSort(arr,left,mid)
    mergeSort(arr,mid+1,right)

    merge(arr,left,mid,right)
    return arr

def merge(arr,left,mid,right):
    temp=[]
    i,j=left,mid+1
    while i<=mid and j<=right:
        if arr[i]<=arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
    while i<=mid:
        temp.append(arr[i])
        i+=1
    while j<=right:
        temp.append(arr[j])
        j+=1
    for k in range(len(temp)):
        arr[left+k]=temp[k]


arr=[15,31,7,83,1,9]
print(mergeSort(arr,0,5))