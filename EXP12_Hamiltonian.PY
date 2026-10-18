def Hamiltonian(n, graph):
    path = [-1] * n
    path[0] = 0

    def Solve(pos):
        if pos == n:
            if graph[path[n - 1]][path[0]] == 1:
                print("Hamiltonian Cycle:", end=" ")
                print(*path, path[0], sep=" -> ")
                return True
            return False

        for v in range(1, n):
            if graph[path[pos - 1]][v] == 1 and v not in path:
                path[pos] = v

                if Solve(pos + 1):
                    return True

                path[pos] = -1

        return False

    if not Solve(1):
        print("No Hamiltonian Cycle exists.")


# Example graph (adjacency matrix)
n = 5
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

Hamiltonian(n, graph)