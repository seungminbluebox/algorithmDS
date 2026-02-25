def floyd(graph):
    n=len(graph)
    dist=[i[:]for i in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j]>dist[i][k]+dist[k][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]

    return dist

INF=float('inf')

graph = [
    [0,     3,     INF,   7],
    [8,     0,     2,     INF],
    [5,     INF,   0,     1],
    [2,     INF,   INF,   0]
]

result = floyd(graph)
for row in result:
    print(row)
# [0, 3, 5, 6]
# [5, 0, 2, 3]
# [3, 6, 0, 1]
# [2, 5, 7, 0]