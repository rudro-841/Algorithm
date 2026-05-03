import heapq

def ucs_path_with_cost(graph, start, end):
    # Priority queue: (cost, node, path)
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node == end:
            return path, cost

        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph[node].items():
                if neighbor not in visited:
                    new_cost = cost + edge_cost
                    new_path = path + [neighbor]
                    heapq.heappush(queue, (new_cost, neighbor, new_path))

    return None, float("inf")


if __name__ == "__main__":
    graph = {
        's': {'a': 5, 'b': 2, 'c': 4},
        'a': {'d': 9, 'e': 4},
        'b': {'g': 6},
        'c': {'f': 2},
        'd': {'h': 7},
        'e': {'g': 6},
        'f': {'g': 1},
        'g': {},
        'h': {}
    }

    source = input("Enter source node: ").strip().lower()
    destination = input("Enter destination node: ").strip().lower()

    path, cost = ucs_path_with_cost(graph, source, destination)

    if path:
        print(f"Optimal path from {source} to {destination}: {' -> '.join(path)}")
        print(f"Total cost: {cost}")
    else:
        print(f"No path found from {source} to {destination}")