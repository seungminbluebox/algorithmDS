def heapify(arr,n,i):
    biggest=i
    left=2*i+1
    right=2*i+2

    if left<n and arr[biggest]<arr[left]:
        biggest=left
    if right<n and arr[biggest]<arr[right]:
        biggest=right
    
    if biggest!=i:
        arr[i],arr[biggest]=arr[biggest],arr[i]
        heapify(arr,n,biggest)

def sort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i) #아래서부터 위로 배열되지않은 상태
    for j in range(n-1,0,-1):
        arr[j],arr[0]=arr[0],arr[j]# 배열됬지만 top이 날아가 가장 작은값이 top에 위치된 상태
        heapify(arr,j,0) # 키큰애 제외하고 다시 힙정렬 실행 위에서부터 아래로
    
data = [12, 11, 13, 5, 6, 7]
sort(data)

print("Sorted array:", data)
# Sorted array: [5, 6, 7, 11, 12, 13]