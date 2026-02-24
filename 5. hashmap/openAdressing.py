class HashMap:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size
        self.DELETE=('deleted',None)

    def toHash(self,key): #key:apple, value:빨간색 과일
        return hash(key)%self.size
    
    def put(self, key, value):
        index=self.toHash(key)
        for i in range(self.size):
            idx=(index+i)%self.size
            item=self.table[idx]
            if item is None or item==self.DELETE:
                self.table[idx]=(key,value)
                return
            if item[0]==key:
                self.table[idx]=(key,value)
                return
    
    def get(self,key):
        index=self.toHash(key)
        for i in range(self.size):
            idx=(index+i)%self.size
            item=self.table[idx]
            if item is None :#애초에 none이였으면 처음부터 변화없었다는뜻이고 여기 인덱스로하는 데이터는 삽입조차된적없으니 바로 none 반환
                return None
            if item[0]==key and item!=self.DELETE: # ('deleted',None)도 사용자가 우연히 delete라는 키값을 사용했다면 none을 반환할수도 있기때문에 조건에 추가해줌
                return item[1]
        return False
#       None: 데이터가 들어온 적 없음 (탐색 종료)

#       DELETED: 데이터가 있었지만 지금은 없음 (건너뛰고 다음 칸 확인)

#       유효한 데이터: 실제 (Key, Value)가 들어있음 (Key가 일치하는지 확인)

    def remove(self,key):
        index=self.toHash(key)
        for i in range(self.size):
            idx=(index+i)%self.size
            item=self.table[idx]
            if item is None:
                return None
            if item!=self.DELETE and item[0]==key:
                self.table[idx]=self.DELETE
                return True
        return False
    
# 1. 해시맵 인스턴스 생성 (사이즈 5)
h_map = HashMap(5)

print("--- 데이터 삽입 ---")
# 2. 데이터 삽입 (put)
h_map.put("apple", "빨간색 과일")
h_map.put("banana", "노란색 과일")
h_map.put("cherry", "작고 빨간 과일")

# 3. 데이터 조회 (get)
print(f"apple: {h_map.get('apple')}")   # 출력: 빨간색 과일
print(f"banana: {h_map.get('banana')}") # 출력: 노란색 과일

print("\n--- 데이터 업데이트 ---")
# 4. 데이터 업데이트 (같은 키에 다른 값)
h_map.put("apple", "맛있는 사과")
print(f"apple 업데이트 후: {h_map.get('apple')}") # 출력: 맛있는 사과

print("\n--- 데이터 삭제 ---")
# 5. 데이터 삭제 (remove)
success = h_map.remove("banana")
print(f"banana 삭제 성공 여부: {success}") # 출력: True

# 6. 삭제 후 조회
print(f"삭제된 banana 조회: {h_map.get('banana')}") # 출력: None

# 7. 존재하지 않는 키 조회
print(f"없는 키(grape) 조회: {h_map.get('grape')}") # 출력: False (작성한 get 로직 기준)