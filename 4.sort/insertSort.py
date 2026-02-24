# def insertSort(arr):
#     n=len(arr)
#     for i in range(1,n):
#         for j in range(i,0,-1):
#             if arr[j-1]>arr[j]:
#                 arr[j-1],arr[j]=arr[j],arr[j-1]
#     return arr

# arr=[5,3,21,8]
# print(insertSort(arr))


def insertSort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

arr=[5,3,21,8]
print(insertSort(arr))