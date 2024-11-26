from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)


    def iddfs(self, start, goal, max_depth):
        for depth in range(max_depth + 1):
            visited = set()
            print(depth)
            if self.dls(start, goal, depth, visited):
                return True
        return False

    def dls(self, node, goal, depth, visited):
        if node == goal:
            return True
        if depth == 0:
            return False
        visited.add(node)
        print(visited)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if self.dls(neighbor, goal, depth - 1, visited):
                    return True
        return False



g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# graph1 = {1: [2, 3], 2: [1, 4, 5], 3: [1, 6, 7], 4: [2], 5: [2], 6: [3], 7: [3]}

start = 0
goal = 3
max_depth = 3
if g.iddfs(start, goal, max_depth):
    print("Path found")
else:
    print("Path not found")
