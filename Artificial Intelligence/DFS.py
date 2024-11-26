from traceback import print_tb


def dfs(graph, start, goal):
    visit = set()
    path = []
    stack = [start]
    path = []

    while stack:
        node = stack.pop()
        if node not in path:
            path.append(node)

        if node not in visit:
            visit.add(node)
            print('node', node, "added")

        if node == goal:
            return visit,path

        for neighbor in graph[node]:
            if neighbor not in visit:
                stack.append(neighbor)






graph1 = {1: [2, 3], 2: [1, 4, 5], 3: [1, 6, 7], 4: [2], 5: [2], 6: [3], 7: [3]}
visit,path = dfs(graph1, 1, 6)
print("Visited Node:",visit)
print("Path:",path)

