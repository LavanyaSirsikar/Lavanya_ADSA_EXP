INF = float('inf')

def floyd_warshall(graph, n):
    
  
    dist = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(graph[i][j])
        dist.append(row)

  
    for k in range(n):
        for i in range(n):
            for j in range(n):
                
         
                if dist[i][k] != INF and dist[k][j] != INF:
                    
                  
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

    print("Shortest Distance Matrix:")

    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                print("INF", end="\t")
            else:
                print(dist[i][j], end="\t")
        print()

    return dist


# Driver Code
graph = [
    [0,   5,   INF, 10],
    [INF, 0,   3,   INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

n = len(graph)

floyd_warshall(graph, n)