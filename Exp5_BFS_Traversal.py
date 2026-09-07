# Simple BFS Traversal in Python

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = [start]
    visited[start] = True
    
    print("BFS Traversal:", end=" ")
    
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    print()

# Example graph (adjacency list)
graph = [
    [1, 2],      # Node 0
    [0, 3],      # Node 1
    [0, 3],      # Node 2
    [1, 2]       # Node 3
]

bfs(graph, 0)            

