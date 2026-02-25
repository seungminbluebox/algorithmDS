import heapq

def dijkstra(adj_list, start_node):
    num_nodes = len(adj_list)
    
    # 1. 각 노드까지의 최단 거리를 무한대로 초기화
    min_distances = [float('inf')] * num_nodes
    min_distances[start_node] = 0
    
    # 2. 탐색 후보를 담는 우선순위 큐 (거리, 노드번호)
    priority_queue = [(0, start_node)]

    while priority_queue:
        # 현재 가장 짧은 거리로 갈 수 있는 노드를 선택
        current_dist, current_node = heapq.heappop(priority_queue)
        
        # 지금 꺼낸 이 경로가 우리가 지금까지 알아낸 최선인가
        # 지금 꺼낸 거리> 해당 노드로 가는 최소거리 라면 아래 반복문 스킵
        if current_dist > min_distances[current_node]:
            continue
            
        # 현재 노드와 연결된 이웃들을 하나씩 확인
        for neighbor_node, weight in adj_list[current_node]:
            # 새로운 경로의 거리 = (현재 노드까지 거리) + (이웃까지의 거리)
            distance_via_current = min_distances[current_node] + weight
            
            # 새로 발견한 경로가 기존에 알던 거리보다 짧다면 업데이트
            if distance_via_current < min_distances[neighbor_node]:
                min_distances[neighbor_node] = distance_via_current
                heapq.heappush(priority_queue, (distance_via_current, neighbor_node))
                
    return min_distances
#list에선 (도착정점,가중치) #heap에선 (거리,도착정점)
def dij(list,startNode):
    n=len(list)
    heap=[(0,startNode)]
    minDistance=[float('inf')]*n
    minDistance[startNode]=0

    while heap:
        currentDistance,currentDesNode=heapq.heappop(heap)

        if minDistance[currentDesNode]<currentDistance:
            continue

        for newDesNode,weight in list[currentDesNode]:
            newDistance=currentDistance+weight

            if newDistance<minDistance[newDesNode]:
                minDistance[newDesNode]=newDistance
                heapq.heappush(heap,(newDistance,newDesNode))
    return minDistance

graph = [
    [(1, 4), (2, 2)],        # 0번 노드와 연결된 노드들
    [(2, 5), (3, 10)],       # 1번 노드와 연결된 노드들
    [(4, 3)],                # 2번 노드와 연결된 노드들
    [(4, 4)],                # 3번 노드와 연결된 노드들
    []                       # 4번 노드와 연결된 노드들 (없음)
]

start = 0
result = dij(graph, start)

print(f"--- {start}번 노드에서 출발한 최단 거리 ---")
for i, dist in enumerate(result):
    print(f"{i}번 노드까지의 거리: {dist}")