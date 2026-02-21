class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoubleLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def addAtHead(self,data):
        newNode=Node(data)
        if not self.head:
            self.head=self.tail=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode

    def addAtTail(self,data):
        newNode=Node(data)
        if not self.tail:
            self.tail=self.head=newNode
        else:
            newNode.prev=self.tail
            self.tail.next=newNode
            self.tail=newNode

    def deleteHead(self):
        if not self.head:
            return
        if self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
    
    def deleteTail(self):
        if not self.tail:
            return
        if self.tail==self.head:
            self.tail=self.head=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None

    def searchFromHeade(self,key):
        current=self.head
        while current:
            if current.data==key:
                return True
            current=current.next
        return False
    
    def searchFromTail(self,key):
        current=self.tail
        while current:
            if current.data==key:
                return True
            current=current.prev
        return False
    
    def traverseHead(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next

    def traverseTail(self):
        current=self.tail
        while current:
            print(current.data)
            current=current.prev