# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 12:21:39 2023

@author: Shivani Gomase
"""

def bfs(graph,root):
    visited, queue= [root], [root]
    while queue:
        vertex = queue.pop(0)
        print(vertex, "popped")
        if vertex in graph.keys():
            for w in graph[vertex]:
                if w not in visited:
                    visited.append(w)
                    queue.append(w)
    print("All nodes traversed")
    return (visited)
tree1={1:[2,3],2:[4,5],3:[6,7]}
graph2={'a':['b','e','c'],
        'b':['a','d','e'],
        'c':['a','f','g'],
        'd':['b','e'],
        'e':['a','b','d'],
        'f':['c'],
        'g':['c']}
v2=bfs(graph2, 'a')
print("BFS Traversal:", v2)              