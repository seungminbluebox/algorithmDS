def binarySearch(arr,target):
    left=0
    right=len(arr)-1
    index=None
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        elif arr[mid]>target:
            right=mid-1
        else:
            return False
arr=[1,2,3,4,5,6,7,8,9]
print(binarySearch(arr,8))