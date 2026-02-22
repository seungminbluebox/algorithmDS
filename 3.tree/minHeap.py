class MinHeap:
    def __init__(self):
        self.heap=[]
    def heapifyUp(self,index):
        parent=(index-1)//2
        if parent>0 and self.heap[index]<self.heap[parent]:
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
