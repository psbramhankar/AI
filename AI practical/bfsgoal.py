def bfs(graph, start, end):
    visited=[]
    queue =[[start]]
    if start==end:
        print('start and end are same')
    while queue:
        pathvertices=queue.pop(0)
        print("pop elements of queue", pathvertices)
        vertex=pathvertices[-1]
        if vertex not in visited:
            visited.append(vertex)
            print("visited nodes:", visited)
            neighbours=graph[vertex]
            for n in neighbours:
                newpath=list(pathvertices)
                newpath.append(n)
                queue.append(newpath)
                print("Path appended in queue",queue,"\n")
                if n==end:
                    return(newpath)
                
graph1={6:[7,8],7:[6,9,8],8:[6,11,12],9:[7],10:[7],11:[8],12:[8]}
v3 = bfs(graph1, 6, 10)
print('Shortest path is:', v3)                