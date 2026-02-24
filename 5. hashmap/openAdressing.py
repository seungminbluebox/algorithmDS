class HashMap:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size
        self.DELETE=("<deleted>",None)
    def toHash(self, key):
        return hash(key)%self.size
    
    def put(self,key,value):
        index=self.toHash(key)
        for i in range(len(self.table)):
            idx=(index+i)%self.size
            item=self.table[idx]
            if item is None:
                self.table[idx] = (key, value)
                return
            if item!=self.DELETE or item[0]==key:
                self.table[idx]=(key,value)
                return
    
    def get(self,key):
        index=self.toHash(key)
        for i in range(len(self.table)):
            idx=(index+i)%self.size
            item=self.table[idx]
            if item is None:
                return False
            if item==self.DELETE:
                continue
            if item[0]==key:
                return item[1]
        return False
    
    def remove(self, key):
        index=self.toHash(key)
        for i in range(len(self.table)):
            idx=(index+i)%self.size
            item=self.table[idx]
            if item is None:
                return False
            if item==self.DELETE:
                continue
            if item[0]==key:
                self.table[idx]=self.DELETE
                return True
            