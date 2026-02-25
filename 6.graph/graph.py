class Graph: #인접리스트로 구현
    def __init__(self,directed=False):
        self.directed=directed #그래프가 일방통행, 양방통행중 하나이고, 이 규칙을 모든 엣지가 따름
        self.list={}
    
    def add(self,start,end,weight=1):
        if start not in self.list: #리스트에 해당 정점으로부터 출발하는 리스트가 없다면
            self.list[start]=[]
        self.list[start].append((end, weight))

        if not self.directed: # 방향성이 없는 선이라면 시작점,끝점 둘다 양쪽으로 연결해야함 근데 그래프의 속성인데 어떻게 엣지의 속성으로 사용하는건가?
            if end not in self.list:
                self.list[end]=[]
            self.list[end].append((end, weight))
        
    def printGraph(self):
        for node in self.list:
            print(f"{node} => {self.list[node]}")


# 그래프 인스턴스 생성 (기본값: 무방향)
undirected_graph = Graph(directed=False)

# 간선 추가 (정점, 목적지, 가중치)
undirected_graph.add("Seoul", "Busan", 400)
undirected_graph.add("Seoul", "Incheon", 50)

print("--- 무방향 그래프 결과 ---")
undirected_graph.printGraph()

class Graph1:
    def __init__(self,size,directed=False):
        self.directed=directed
        self.size=size
        self.list=[[0]*size for i in range(size)]

    def add(self,start,end,weight=1):
        self.list[start][end]=weight
        if not self.directed:
            self.list[end][start]=weight

    def printG(self):
        for i in self.list:
            print(i)

# 정점 3개짜리 무방향 그래프 생성 (0, 1, 2번 정점 사용 가능)
undirected_matrix = Graph1(size=3, directed=False)

# 간선 추가
undirected_matrix.add(0, 1, 5)  # 0번과 1번 사이 가중치 5
undirected_matrix.add(1, 2, 10) # 1번과 2번 사이 가중치 10

print("--- 무방향 인접 행렬 결과 ---")
undirected_matrix.printG()