def bfs_path_with_cost(graph, start, end):
    
    queue = [(start, [start], 0)]
    visited = set()

    while queue:
        
        node, path, cost = queue.pop(0)

        if node == end:
            return path, cost

        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph[node].items():
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor], cost + edge_cost))

    return None, float("inf")


if __name__ == "__main__":
    graph = {
        's': {'a': 5, 'b': 2, 'c': 4},
        'a': {'d': 9, 'e': 4},
        'b': {'g': 6},
        'c': {'f': 2},
        'd': {'h':7},
        'e': {'g': 6},
        'g': {},
        'f': {'g': 1},
        'h': {}
    }


    source = input("Enter source node: ").strip()
    destination = input("Enter destination node: ").strip()

    path, cost = bfs_path_with_cost(graph, source, destination)

    if path:
        print(f"Path from {source} to {destination}: {' -> '.join(path)}")
        print(f"Total cost: {cost}")
    else:
        print(f"No path found from {source} to {destination}")
