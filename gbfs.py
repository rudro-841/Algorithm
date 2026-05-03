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


def greedy_best_first_search(graph, start, end, heuristic):
    # Priority queue: (heuristic_cost, node, path, actual_cost)
    queue = [(heuristic(start, end), start, [start], 0)]
    visited = set()

    while queue:
        h_cost, node, path, actual_cost = heapq.heappop(queue)

        if node == end:
            return path, actual_cost

        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph[node].items():
                if neighbor not in visited:
                    new_actual_cost = actual_cost + edge_cost
                    new_h_cost = heuristic(neighbor, end)
                    new_path = path + [neighbor]
                    heapq.heappush(queue, (new_h_cost, neighbor, new_path, new_actual_cost))

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

    # Define a simple heuristic (Manhattan distance-like estimate)
    heuristic_values = {
        's': 10, 'a': 8, 'b': 7, 'c': 6,
        'd': 5, 'e': 4, 'f': 3, 'g': 0, 'h': 2
    }

    def heuristic(node, goal):
        return heuristic_values.get(node, 0)

    source = input("Enter source node: ").strip()
    destination = input("Enter destination node: ").strip()

    print("\n--- UCS (Uniform Cost Search) ---")
    path_ucs, cost_ucs = ucs_path_with_cost(graph, source, destination)
    if path_ucs:
        print(f"Path from {source} to {destination}: {' -> '.join(path_ucs)}")
        print(f"Total cost: {cost_ucs}")
    else:
        print(f"No path found from {source} to {destination}")

    print("\n--- GBFS (Greedy Best First Search) ---")
    path_gbfs, cost_gbfs = greedy_best_first_search(graph, source, destination, heuristic)
    if path_gbfs:
        print(f"Path from {source} to {destination}: {' -> '.join(path_gbfs)}")
        print(f"Total cost: {cost_gbfs}")
    else:
        print(f"No path found from {source} to {destination}")
