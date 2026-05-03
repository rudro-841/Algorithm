import heapq

def ucs_path_with_cost(graph, start, end):
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
                    heapq.heappush(queue, (cost + edge_cost, neighbor, path + [neighbor]))

    return None, float("inf")


def greedy_best_first_search(graph, start, end, heuristic):
    queue = [(heuristic(start), start, [start], 0)]
    visited = set()

    while queue:
        h_cost, node, path, actual_cost = heapq.heappop(queue)

        if node == end:
            return path, actual_cost

        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(queue, (heuristic(neighbor), neighbor,
                                           path + [neighbor], actual_cost + edge_cost))

    return None, float("inf")


def print_result(label, source, destination, path, cost):
    print(f"\n--- {label} ---")
    if path:
        print(f"Path from {source} to {destination}: {' -> '.join(path)}")
        print(f"Total cost: {cost}")
    else:
        print(f"No path found from {source} to {destination}")


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

    heuristic_values = {
        's': 10, 'a': 8, 'b': 7, 'c': 6,
        'd': 5,  'e': 4, 'f': 3, 'g': 0, 'h': 2
    }

    heuristic = lambda node: heuristic_values.get(node, 0)  # goal removed — wasn't used

    source = input("Enter source node: ").strip()
    destination = input("Enter destination node: ").strip()

    print_result("UCS", source, destination,
                 *ucs_path_with_cost(graph, source, destination))

    print_result("GBFS", source, destination,
                 *greedy_best_first_search(graph, source, destination, heuristic))