### 기초
arr=[123,48,56,78,90]
print(arr[0]) #123 복잡도 O(1)

for i in arr: # 복잡도 O(n)
    if i==56:
        print("Found" + str(i))
        break

### 정적배열과 동적배열
## 정적배열은 크기가 고정되어있음
## 동적배열은 크기가 가변적임
del arr[0] # O(n)
print(arr) #[48, 56, 78, 90]

arr.append(100) # O(1)
arr.insert(0, 123) # O(n)
print(arr) #[123, 48, 56, 78, 90, 100]

### 2차원 배열
arr2d=[[1,2,3],[4,5,6],[7,8,9]]
# 탐색
print(arr2d[0][0]) #1 복잡도 O(1)
# 수정
arr2d[0][0]=10 # O(1)
print(arr2d) #[[10, 2, 3], [4, 5, 6], [7, 8, 9]]
# 탐색 및 수정
for i in range(len(arr2d)):
    for j in range(len(arr2d[i])):
        if arr2d[i][j]==5:
            print("Found at position (" + str(i) + "," + str(j) + ")") # O(n^2) Found at position (1,1)
# 전부 탐색
for i in range(len(arr2d)):
    for j in range(len(arr2d[i])):
        print(arr2d[i][j], end=" ") # O(n^2) 10 2 3 4 5 6 7 8 9 
    print()