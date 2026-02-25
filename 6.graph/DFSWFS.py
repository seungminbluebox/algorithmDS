from collections import deque


class Graph:
    def __init__(self,size):
        self.size=size
        self.list={i:[]for i in range(size)}

    def add(self,start,end):
        self.list[start].append(end)
        self.list[end].append(start)

    def dfs(self,start):
        visited=set()
        def visit(start):
            visited.add(start)
            print(f"visit : {start}")
            for i in self.list[start]:
                if i not in visited:
                    visit(i)
        visit(start)

    def bfs(self,start):
        visited=set()
        queue=deque([start])
        visited.add(start)
        while queue:
            v=queue.popleft()
            print(f"visit : {v}")
            for i in self.list[v]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)


g = Graph(5)
g.add(0, 1)
g.add(0, 2)
g.add(1, 3)
g.add(1, 4)

print("DFS:")
g.dfs(0)  # 0 1 3 4 2

print("BFS:")
g.bfs(0)  # 0 1 2 3 4