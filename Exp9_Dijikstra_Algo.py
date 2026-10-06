import heapq

def dijkstra(graph, source):
    n = len(graph)
    distance = [float('inf')] * n
    distance[source] = 0

    pq = [(0, source)]

    while pq:
        dist, u = heapq.heappop(pq)

        if dist > distance[u]:
            continue

        for v in range(n):
            if graph[u][v] != 0:
                new_dist = dist + graph[u][v]

                if new_dist < distance[v]:
                    distance[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

    return distance


# Adjacency matrix
graph = [
    [0, 4, 1, 0, 0],
    [4, 0, 2, 5, 0],
    [1, 2, 0, 8, 10],
    [0, 5, 8, 0, 2],
    [0, 0, 10, 2, 0]
]

source = 0

print("Shortest distances:", dijkstra(graph, source))