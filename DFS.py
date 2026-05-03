import collections

def dfs(graph, root):
    visited = set()
    stack = collections.deque([root])
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for i in graph[vertex]:
                if i not in visited:
                    stack.append(i)

    print("Visited nodes:", visited)


def dfs_path_with_cost(graph, start, end):
    visited = set()
    stack = collections.deque([(start, [start], 0)])
    while stack:
        node, path, cost = stack.pop()
        if node == end:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbour, edge_cost in graph[node].items():
                if neighbour not in visited:
                    stack.append((neighbour, path + [neighbour], cost + edge_cost))

    return None, float("inf")


def main():
    graph = {
        's': {'a': 5, 'b': 2, 'c': 4},
        'a': {'d': 9, 'e': 4},
        'b': {'g': 6},
        'c': {'f': 2},
        'd': {'h': 7},
        'e': {'g': 6},
        'g': {},
        'f': {'g': 1},
        'h': {}
    }

    print("--- DFS Traversal ---")
    dfs(graph, 's')

    print("\n--- DFS Path Finder ---")
    source = input("Enter source node: ").strip()
    destination = input("Enter destination node: ").strip()

    path, cost = dfs_path_with_cost(graph, source, destination)

    if path:
        print(f"Path from {source} to {destination}: {' -> '.join(path)}")
        print(f"Total cost: {cost}")
    else:
        print(f"No path found from {source} to {destination}")


if __name__ == "__main__":
    main()