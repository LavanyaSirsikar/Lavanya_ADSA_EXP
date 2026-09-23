import sys

def min_key(vertices_count, key, mst_set):
    """Finds the vertex with the minimum key value from the set of vertices not yet included in the MST."""
    min_val = sys.maxsize
    min_index = -1
    
    for v in range(vertices_count):
        if key[v] < min_val and not mst_set[v]:
            min_val = key[v]
            min_index = v
            
    return min_index

def prim_mst(graph):
    """Computes and prints the Minimum Spanning Tree (MST) using Prim's algorithm."""
    vertices_count = len(graph)
    
    # Array to store constructed MST
    parent = [None] * vertices_count 
    # Key values used to pick minimum weight edge
    key = [sys.maxsize] * vertices_count 
    # To represent set of vertices included in MST
    mst_set = [False] * vertices_count 

    # Start from vertex 0
    key[0] = 0
    parent[0] = -1 

    for _ in range(vertices_count - 1):
        # Pick the minimum key vertex not yet in MST
        u = min_key(vertices_count, key, mst_set)

        # Add the picked vertex to the MST set
        mst_set[u] = True

        # Update key and parent of adjacent vertices
        for v in range(vertices_count):
            # graph[u][v] is non-zero only if there is an edge
            # mst_set[v] is False for vertices not yet included in MST
            # Update the key only if graph[u][v] is smaller than key[v]
            if 0 < graph[u][v] < key[v] and not mst_set[v]:
                parent[v] = u
                key[v] = graph[u][v]

    # Print the constructed MST
    print("Edge \tWeight")
    for i in range(1, vertices_count):
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")

# --- Example Usage ---
if __name__ == "__main__":
    # Representing the graph using a 5x5 adjacency matrix
    example_graph = [,
 ,
 ,
 ,
        [0, 5, 7, 9, 0]
    ]

    prim_mst(example_graph)
