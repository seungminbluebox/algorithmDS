class HashMap:
    def __init__(self,size):
        self.size=size
        self.table=[[] for i in range(size)]
    def toHash(self,key):
        return hash(key)%self.size
    
    def put(self,key,value):
        index=self.toHash(key)
        for i in self.table[index]:
            if i[0]==key:
                i[1]=value # 키값이 같다면 내용만 업데이트
                return
        self.table[index].append([key,value])
    def get(self,key):
        index=self.toHash(key)
        for i in self.table[index]:
            if i[0]==key:
                return i[1]
        return False
    def remove(self,key):
        index=self.toHash(key)
        # enumerate를 사용하여 요소(pair)와 인덱스(j)를 동시에 가져옴
        for i,pair in enumerate(self.table[index]):
            if pair[0]==key:
                del self.table[index][i]
                return True
        return False
    
# 1. 해시맵 생성 (크기 5)
my_map = HashMap(5)

# 2. 데이터 삽입 (put)
my_map.put("name", "Alice")
my_map.put("age", 25)
my_map.put("city", "Seoul")

# 3. 데이터 조회 (get)
print(f"이름: {my_map.get('name')}") # 출력: Alice
print(f"나이: {my_map.get('age')}")  # 출력: 25

# 4. 데이터 업데이트 (기존 키에 다른 값 넣기)
my_map.put("age", 26)
print(f"수정된 나이: {my_map.get('age')}") # 출력: 26

# 5. 데이터 삭제 (remove)
is_removed = my_map.remove("city")
print(f"삭제 성공 여부: {is_removed}") # 출력: True

# 6. 삭제 후 조회
print(f"삭제된 도시 조회: {my_map.get('city')}") # 출력: False (데이터 없음)

# 7. 없는 키 삭제 시도
print(f"없는 키 삭제 결과: {my_map.remove('hobby')}") # 출력: False