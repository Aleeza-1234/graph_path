# Graph construction
data = [(1, 2, 2), (2, 4, 2), (1, 3, 4), (3, 4, 1)]
queries = [(1, 4, 2), (2, 3, 1)]

# Convert data into adjacency list using a normal dictionary
graph = {}
for u, v, w in data:
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, w))
    graph[v].append((u, w))  

# Function to find the path from start to end using BFS
def find_path(start, end):
    queue = [(start, [])]  
    visited = set()

    while queue:
        node, path = queue.pop(0) 
        if node == end:
            return path  

        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph.get(node, []):  
            if neighbor not in visited:
                queue.append((neighbor, path + [weight]))

    return []  

# Processing queries
sol = []
for a, b, k in queries:
    path_weights = find_path(a, b)
    
    if len(path_weights) >= k:
        path_weights.sort(reverse=True)  
        sol.append(path_weights[k-1])
    else:
        sol.append(-1)  

print(sol)

                
                
