

def dfs(graph,start,goal):
    visited = set()
    stack = [start]
    path=[]
    while stack:
        node = stack.pop()
        if node not in path:
            path.append(node)
        if node not in visited:
            visited.add(node)
            print('node',node,"added")
        if node ==goal:
            return visited
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
graph1 = {1:[2,3],2:[1,4,5],3:[1,6,7],4:[2],5:[2],6:[3],7:[3]}
visited = dfs(graph1,1,7)
print(visited)
               