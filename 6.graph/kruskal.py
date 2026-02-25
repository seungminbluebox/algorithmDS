N = 4  # number of vertices
edges = [
    [0, 1, 1],
    [0, 2, 4],
    [1, 2, 2],
    [1, 3, 6],
    [2, 3, 3]
]

parent=[i for i in range(N)]
def findRoot(x): #해당 요소의 root를 찾기
    if parent[x]!=x:
        parent[x]=findRoot(parent[x])
        return parent[x]
    return parent[x]

def union(x,y): #서로 root가 다르다면 x,y를 연결할수있음-true반환
    xRoot=findRoot(x)
    yRoot=findRoot(y)
    if xRoot!=yRoot:
        parent[yRoot]=xRoot
        return True
    else:
        return False
    
edges.sort(key=lambda x:x[2]) #가중치가 가장 적은것부터 나열해서 하나씩 union작업
w=0
for start,end,weight in edges:
    if union(start,end): #서로 root가 달라서 x,y를 연결했다면
        w+=weight        #그에맞는 가중치를 더한다

print("MST Weight:", w)