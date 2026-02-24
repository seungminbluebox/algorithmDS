class MinHeap:
    def __init__(self):
        self.heap=[]
    def heapifyUp(self,index):
        parent=(index-1)//2
        if index>0 and self.heap[index]<self.heap[parent]:
            self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
            self.heapifyUp(parent)

    def heapifyDown(self,index):
        smallest=index
        left=2*index+1
        right=2*index+2
        size=len(self.heap)

        if left<size and self.heap[left]<self.heap[smallest]:
            smallest=left
        if right<size and self.heap[right]<self.heap[smallest]:
            smallest=right

        if smallest!=index:
            self.heap[index],self.heap[smallest]=self.heap[smallest],self.heap[index]
            self.heapifyDown(smallest)

    def buildHeap(self,arr):
        self.heap=arr[:]
        for i in range((len(self.heap)//2)-1,-1,-1):
            self.heapifyDown(i)
    
    def insert(self,data):
        self.heap.append(data)
        self.heapifyUp(len(self.heap)-1)

    def getMin(self):
        if not self.heap:
            return False
        return self.heap[0]
    
    def removeMin(self):
        if not self.heap:
            return False
        min=self.heap[0]
        last=self.heap.pop()
        if self.heap:
            self.heap[0]=last
            self.heapifyDown(0)
        return min

# 1. 힙 객체 생성
my_heap = MinHeap()

# 2. 무작위 배열을 한 번에 힙으로 만들기 (buildHeap 검증)
print("- buildHeap 작동 확인 -")
unsorted_array = [30, 10, 50, 20, 40]
my_heap.buildHeap(unsorted_array)
print(f"무작위 배열이 힙 구조로 변환됨: {my_heap.heap}") 
# 결과 예상: [10, 20, 50, 30, 40] (루트가 10으로 가장 작게 재배치됨)

# 3. 새로운 데이터 삽입 (insert 및 heapifyUp 검증)
print("\n- 데이터 5 삽입 -")
my_heap.insert(5)
print(f"5가 루트로 뚫고 올라온 힙 상태: {my_heap.heap}")

# 4. 힙 정렬 (Heap Sort) 효과 증명 (removeMin 검증)
# 최솟값을 계속 뽑아내면 자연스럽게 오름차순 정렬이 됩니다.
print("\n- 데이터 연속 추출 (오름차순 정렬 증명) -")
sorted_result = []
while my_heap.heap: # 힙이 빌 때까지 반복
    sorted_result.append(my_heap.removeMin())

print(f"추출된 순서: {sorted_result}")