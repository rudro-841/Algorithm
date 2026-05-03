def bfs_traversal(graph,start,end):
    queue=[(start,[start],0)]
    visited=set()
    
    
    while queue:
        node,path,cost=queue.pop(0)
        
        if node ==end:
            return path,cost
        
        if node not in visited :
            visited.add(node)
            for neighbour, edge_cost in graph[node].items():
                if neighbour not in visited:
                    queue.append((neighbour,path+[neighbour],cost+edge_cost))
                    
    return None, float("inf")


def main():
    graph ={'s': {'a': 5, 'b': 2, 'c': 4},
        'a': {'d': 9, 'e': 4},
        'b': {'g': 6},
        'c': {'f': 2},
        'd': {'h':7},
        'e': {'g': 6},
        'g': {},
        'f': {'g': 1},
        'h': {}}
    
    source=input("Enter the source : ").strip().lower()
    destination= input("Enter the destination :").strip().lower()
    path,cost=bfs_traversal(graph,source,destination)
    if path:
        print(f"the path form {source} to {destination} is  : {'->'.join(path)}")
    else :
        print("No destination")
        
    

if __name__=="__main__":
    main()
    
    