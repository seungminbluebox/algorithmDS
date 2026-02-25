import heapq


N = 4  # number of vertices
graph = [[] for _ in range(N)]
edges = [
    [0, 1, 1],
    [0, 2, 4],
    [1, 2, 2],
    [1, 3, 6],
    [2, 3, 3]
]

for start,end,weight in edges:
    graph[start].append((end,weight))
    graph[end].append((start,weight))

visited=[False]*N
heap=[(0,0)] # (가중치, 도착점)
totalWeight=0
while heap:
    weight,destNode=heapq.heappop(heap)
    if visited[destNode]==True:
        continue
    visited[destNode]=True
    totalWeight+=weight
    for endNode, edge_weight in graph[destNode]:
        if visited[endNode]==False:
            heapq.heappush(heap, (edge_weight, endNode))

print(f"최소 신장 트리 총 가중치: {totalWeight}")