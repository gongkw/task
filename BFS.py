graph ={"A":["B","C","D"],
       "B":["C","D"],
       "C":["D","E","A"],
      "D":["A","B","C"],
      "E":["A","B","C","D","E"]       
}

def BFS(graph, s):
    queue=[]
    seen=set()
    seen.add(s)
    queue.append(s)
    parent={s:None}
    while (len(queue) > 0):
        vertex = queue.pop(0)
        for node in graph[vertex]:
            if node not in seen:
                queue.append(node)
                seen.add(node)
                parent[node] = vertex
        print vertex
    print parent

parent = BFS(graph,"A")

# v="B"

# while v != None:
#     print v
#     v = parent[v]

            

