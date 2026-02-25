def bell(n,edge,start):
    dist=[float('inf')]*n
    dist[start]=0

    for i in range(n-1):
        for start,end,weight in edge:
            if dist[start]+weight<dist[end]:
                dist[end]=dist[start]+weight
    
    for start,end,weight in edge:
        if dist[start]+weight<dist[end]:
            return False
        
    return dist

# --- 데이터 준비 ---
# 정점 개수: 5개 (0, 1, 2, 3, 4)
n = 5
# 간선 정보 (시작, 끝, 가중치)
# 음수 가중치(-1, -2 등)가 포함되어 있습니다.
edges = [
    (0, 1, 6),
    (0, 2, 7),
    (1, 2, 8),
    (1, 3, 5),
    (1, 4, -4), # 음수 가중치
    (2, 3, -3), # 음수 가중치
    (2, 4, 9),
    (3, 1, -2), # 음수 가중치
    (4, 0, 2),
    (4, 3, 7)
]

# 0번 노드에서 출발
start_point = 0
result = bell(n, edges, start_point)

# 결과 출력
if result is False:
    print("그래프에 음수 사이클이 존재하여 최단 거리를 정의할 수 없습니다-")
else:
    print(f"[{start_point}번 노드 출발 최단 거리 결과]")
    for i, distance in enumerate(result):
        print(f"{i}번 노드까지의 거리: {distance}")